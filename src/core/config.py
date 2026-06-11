"""
Lab 11 — Configuration & API Key Setup
"""
import os
from dotenv import load_dotenv

load_dotenv()

def setup_api_key():
    # """Load Google API key from environment or prompt."""
    # if "GOOGLE_API_KEY" not in os.environ:
    #     os.environ["GOOGLE_API_KEY"] = input("Enter Google API Key: ")
    # os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"
    os.environ["DASHSCOPE_API_KEY"] = os.getenv("DASHSCOPE_API_KEY")
    # Ánh xạ DASHSCOPE_URL sang DASHSCOPE_API_BASE cho LiteLLM nhận diện
    os.environ["DASHSCOPE_API_BASE"] = os.getenv("DASHSCOPE_URL")
    print("API key loaded.")
    print("API key loaded.")


# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
