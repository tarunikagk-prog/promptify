from .config import BASELINE_INPUT_PER_1M, BASELINE_OUTPUT_PER_1M


def estimate_tokens(text: str) -> int:
    return max(1, int(len(text.split()) * 1.35))


def extract_usage_tokens(response, input_text: str, output_text: str) -> tuple[int, int]:
    meta = getattr(response, "usage_metadata", None)
    in_tok = getattr(meta, "prompt_token_count", None) if meta else None
    out_tok = getattr(meta, "candidates_token_count", None) if meta else None

    if in_tok is None:
        in_tok = estimate_tokens(input_text)
    if out_tok is None:
        out_tok = estimate_tokens(output_text)

    return int(in_tok), int(out_tok)


def compute_cost_usd(in_tokens: int, out_tokens: int, in_rate: float, out_rate: float) -> float:
    return (in_tokens / 1_000_000) * in_rate + (out_tokens / 1_000_000) * out_rate


def build_efficiency_report(
    opt_in: int,
    opt_out: int,
    opt_cost: float,
    exec_in: int,
    exec_out: int,
    exec_cost: float,
    elapsed_ms: float,
) -> dict:
    total_actual_cost = opt_cost + exec_cost
    frontier_baseline_cost = compute_cost_usd(
        exec_in, exec_out, BASELINE_INPUT_PER_1M, BASELINE_OUTPUT_PER_1M
    )
    net_savings = frontier_baseline_cost - total_actual_cost
    savings_pct = (
        round((net_savings / frontier_baseline_cost) * 100, 1)
        if frontier_baseline_cost > 0
        else 0.0
    )
    total_tokens = opt_in + opt_out + exec_in + exec_out
    tokens_per_sec = round(total_tokens / max(elapsed_ms / 1000.0, 0.001), 1)

    return {
        "optimizer": {
            "input_tokens": opt_in,
            "output_tokens": opt_out,
            "cost_usd": round(opt_cost, 6),
        },
        "execution": {
            "input_tokens": exec_in,
            "output_tokens": exec_out,
            "cost_usd": round(exec_cost, 6),
        },
        "total_tokens": total_tokens,
        "total_actual_cost_usd": round(total_actual_cost, 6),
        "frontier_baseline_cost_usd": round(frontier_baseline_cost, 6),
        "net_savings_usd": round(net_savings, 6),
        "savings_vs_frontier_pct": savings_pct,
        "latency_ms": round(elapsed_ms, 1),
        "tokens_per_sec": tokens_per_sec,
    }
