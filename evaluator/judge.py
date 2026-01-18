from evaluator.llm_client import call_llm

JUDGE_MODEL = "openai/gpt-4o-mini"


def llm_judge(prompt, response, expected):
    judge_prompt = f"""
You are evaluating an LLM response.

Prompt:
{prompt}

Expected Answer:
{expected}

Model Response:
{response}

Score the response from 1 to 5 on:
1. Relevance
2. Hallucination (5 = no hallucination)
3. Instruction Following

Return ONLY JSON in this format:
{{
  "relevance": number,
  "hallucination": number,
  "instruction": number
}}
"""

    output, _ = call_llm(judge_prompt, JUDGE_MODEL)

    try:
        scores = eval(output)
    except:
        scores = {"relevance": 2, "hallucination": 2, "instruction": 2}

    return scores
