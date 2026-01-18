import json
import pandas as pd
from evaluator.evaluator import evaluate_prompt
from evaluator.aggregator import aggregate_scores


def load_prompts(path):
    with open(path, "r") as f:
        return json.load(f)


def main():
    prompts = load_prompts("prompts/factual.json")
    all_results = []

    for p in prompts:
        print(f"Evaluating: {p['id']}")
        results = evaluate_prompt(p)
        all_results.extend(results)

    # Save raw results
    df = pd.DataFrame(all_results)
    df.to_csv("results/results.csv", index=False)

    # Aggregate scores
    summary_df = aggregate_scores(df)
    summary_df.to_csv("results/summary.csv", index=False)

    print("\n✅ Evaluation complete.")
    print("📄 results/results.csv")
    print("📊 results/summary.csv")

    # Best model
    best = summary_df.sort_values("final_score", ascending=False).iloc[0]
    print("\n🏆 BEST MODEL:")
    print(best)


if __name__ == "__main__":
    main()
