# Promptify — Responsible AI & Resource Optimization

Promptify takes general user prompts, applies pre-flight PII and safety checks, rewrites vague prompts into structured prompts, routes execution to an appropriate Gemini tier, and computes cost and throughput from real token telemetry.

## Features
- **Prompt Refiner:** Turns broad or underspecified prompts into structured instructions with clear context, constraints, and output format.
- **Guardrails & Redaction:** Detects and redacts common PII (emails, phone numbers) and flags restricted terms before model calls.
- **Complexity-Based Tier Routing:** Routes requests across lightweight, balanced, and frontier Gemini models.
- **Verifiable Token & Cost Accounting:** Reads `usage_metadata` token counts (`prompt_token_count` and `candidates_token_count`) and calculates cost using separate input and output rates per 1M tokens.
- **Focused Multi-Tab UI:** Shows the refined prompt, recommended model, and response first, with separate tabs for efficiency math, fairness checks, and prompt comparison.

## Quick Start

```bash
pip install -r requirements.txt
export GEMINI_API_KEY="your-gemini-api-key"
python -m backend.app
