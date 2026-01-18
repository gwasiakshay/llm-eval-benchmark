import pandas as pd

WEIGHTS = {"relevance": 0.4, "hallucination": 0.3, "instruction": 0.2, "latency": 0.1}


def aggregate_scores(df):
    summary = []

    for model in df["model"].unique():
        model_df = df[df["model"] == model]

        avg_relevance = model_df["relevance"].mean()
        avg_hallucination = model_df["hallucination"].mean()
        avg_instruction = model_df["instruction"].mean()
        avg_latency = model_df["latency"].mean()

        final_score = (
            avg_relevance * WEIGHTS["relevance"]
            + avg_hallucination * WEIGHTS["hallucination"]
            + avg_instruction * WEIGHTS["instruction"]
            + (1 / avg_latency) * WEIGHTS["latency"]
        )

        summary.append(
            {
                "model": model,
                "avg_relevance": round(avg_relevance, 2),
                "avg_hallucination": round(avg_hallucination, 2),
                "avg_instruction": round(avg_instruction, 2),
                "avg_latency": round(avg_latency, 2),
                "final_score": round(final_score, 3),
            }
        )

    return pd.DataFrame(summary)
