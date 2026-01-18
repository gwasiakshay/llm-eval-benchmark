from evaluator.llm_client import call_llm
from evaluator.judge import llm_judge
from config import MODELS


def evaluate_prompt(prompt_obj):
    results = []

    for model in MODELS:
        output, latency = call_llm(prompt_obj["prompt"], model)

        scores = llm_judge(prompt_obj["prompt"], output, prompt_obj["expected_answer"])

        results.append(
            {
                "model": model,
                "prompt_id": prompt_obj["id"],
                "prompt": prompt_obj["prompt"],
                "response": output,
                "latency": latency,
                **scores,
            }
        )

    return results
