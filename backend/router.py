from .config import MODEL_TIERS

COMPLEX_SIGNALS = [
    "architecture",
    "compare",
    "trade-off",
    "tradeoff",
    "optimize",
    "algorithm",
    "debug",
    "analyze",
    "design",
    "edge cases",
    "multi-step",
]


def select_model_tier(prompt: str) -> tuple[str, dict, str]:
    lowered = prompt.lower()
    signal_hits = sum(1 for kw in COMPLEX_SIGNALS if kw in lowered)
    length_bonus = 1 if len(prompt) > 160 else 0
    score = signal_hits + length_bonus

    if score >= 3:
        tier_key = "frontier"
        reason = "High complexity or multi-constraint request routed to Frontier tier."
    elif score == 2 or len(prompt) > 85:
        tier_key = "balanced"
        reason = "Moderate scope routed to Balanced tier for strong quality vs. cost."
    else:
        tier_key = "lightweight"
        reason = "Concise or straightforward prompt routed to Lightweight tier to save compute."

    return tier_key, MODEL_TIERS[tier_key], reason
