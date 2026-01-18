🧠 LLM Evaluation & Benchmarking Framework

A lightweight and extensible framework for evaluating and benchmarking Large Language Models (LLMs) using LLM-as-a-Judge, structured scoring, and multi-model comparison.

This project simulates real-world LLM evaluation workflows used in AI product development, model selection, and prompt optimization.

🚀 Features

✅ Multi-model evaluation (GPT-4o, GPT-3.5, etc.)

✅ LLM-as-a-judge scoring

✅ Evaluation metrics:

Relevance

Hallucination

Instruction adherence

Response latency

✅ Weighted score aggregation

✅ Automatic best-model selection

✅ CSV-based result export

✅ Clean, modular Python architecture

📁 Project Structure

llm-eval-benchmark/
│
├── evaluator/
│   ├── llm_client.py        # LLM API calls
│   ├── evaluator.py         # Core evaluation logic
│   ├── judge.py             # LLM-as-a-judge scoring
│   ├── scorer.py            # Metric helpers
│   └── aggregator.py        # Score aggregation & ranking
│
├── prompts/
│   ├── factual.json
│   └── instructions.json
│
├── results/
│   ├── results.csv          # Raw evaluation output
│   └── summary.csv          # Aggregated scores
│
├── runner.py                # Main execution script
├── config.py
├── requirements.txt
└── README.md


🧠 How It Works

Prompts are loaded from JSON files

Each prompt is evaluated across multiple LLMs

Responses are scored using:

LLM-as-a-judge

Structured evaluation logic

Scores are aggregated using weighted metrics

The best-performing model is automatically selected

📊 Evaluation Metrics
Metric	Description
Relevance	How accurately the response answers the prompt
Hallucination	Whether the response contains incorrect facts
Instruction	Adherence to prompt constraints
Latency	Response time of the model

Each metric contributes to a final weighted score.

▶️ How to Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Set environment variable
Create a .env file:
OPENROUTER_API_KEY=your_api_key_here

3️⃣ Run evaluation
python runner.py

📈 Output
results/results.csv

Contains raw model responses and individual scores.

results/summary.csv

Contains aggregated results and final model rankings.

Example:

Model	Final Score
openai/gpt-4o-mini	4.54
openai/gpt-3.5-turbo	3.78
🏆 Best Model Selection

The framework automatically selects the best-performing model based on:

Accuracy

Hallucination risk

Instruction adherence

Latency

This mirrors how LLMs are evaluated in production systems.

🧭 Roadmap
🔹 Upcoming Enhancements

📊 Streamlit dashboard for visual analysis

🔁 Prompt variation testing

🧠 RAG-based evaluation support

⚙️ Config-driven scoring (YAML)

🔄 CI-based evaluation pipeline

💡 Why This Project Matters

This project demonstrates:

Practical LLM evaluation techniques

Model benchmarking and comparison

Prompt engineering analysis

Real-world LLMOps thinking

Production-style project structuring

👨‍💻 Author

Akshay Gwasikoti
AI Automation | LLM Evaluation | Applied AI Engineering
