import re
from .config import UNSAFE_KEYWORDS

PII_PATTERNS = {
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "phone": r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b",
}


def scan_prompt(prompt: str) -> dict:
    sanitized = prompt
    redacted_types = []

    for label, pattern in PII_PATTERNS.items():
        if re.search(pattern, sanitized):
            redacted_types.append(label)
            sanitized = re.sub(pattern, f"[REDACTED_{label.upper()}]", sanitized)

    lowered = prompt.lower()
    flagged_terms = [kw for kw in UNSAFE_KEYWORDS if kw in lowered]
    blocked = len(flagged_terms) > 0

    if blocked:
        status = "FLAGGED"
    elif redacted_types:
        status = "REDACTED"
    else:
        status = "PASS"

    return {
        "status": status,
        "blocked": blocked,
        "flagged_terms": flagged_terms,
        "redacted_types": redacted_types,
        "sanitized_prompt": sanitized,
    }
