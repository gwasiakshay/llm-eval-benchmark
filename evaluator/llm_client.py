import requests
import time
from config import OPENROUTER_API_KEY, BASE_URL, MODELS


def call_llm(prompt, model):
    start_time = time.time()

    response = requests.post(
        BASE_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={"model": model, "messages": [{"role": "user", "content": prompt}]},
    )

    latency = round(time.time() - start_time, 2)
    output = response.json()["choices"][0]["message"]["content"]

    return output, latency
