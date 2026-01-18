import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODELS = ["openai/gpt-4o-mini", "openai/gpt-3.5-turbo"]


BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
