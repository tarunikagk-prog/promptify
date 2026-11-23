MODEL_TIERS = {
    "lightweight": {
        "tier": "Lightweight / Budget",
        "model_id": "gemini-3.5-flash-lite",
        "display_name": "Gemini 3.5 Flash-Lite",
        "quality_index": 0.84,
        "input_per_1m": 0.30,
        "output_per_1m": 2.50,
    },
    "balanced": {
        "tier": "Balanced / High-Throughput",
        "model_id": "gemini-3.8-flash",
        "display_name": "Gemini 3.8 Flash",
        "quality_index": 0.90,
        "input_per_1m": 0.75,
        "output_per_1m": 3.75,
    },
    "frontier": {
        "tier": "Frontier / Deep Reasoning",
        "model_id": "gemini-4-argon",
        "display_name": "Gemini 4 Argon",
        "quality_index": 0.95,
        "input_per_1m": 2.00,
        "output_per_1m": 10.00,
    },
}

BASELINE_INPUT_PER_1M = 2.00
BASELINE_OUTPUT_PER_1M = 10.00

UNSAFE_KEYWORDS = [
    "bypass safety",
    "exploit",
    "malware",
    "hate speech",
]
