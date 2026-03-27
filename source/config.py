import os
from pathlib import Path
from dotenv import load_dotenv

# ==============================
# Load .env (LOCAL)
# ==============================
load_dotenv()

# ==============================
# Base Directory (ONLY ONCE)
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# Paths (KEEP ONLY ONE VERSION)
# ==============================
JSON_PATH = BASE_DIR / "data" / "clean" / "visa_policy.json"
VECTOR_DB_PATH = BASE_DIR / "Output" / "Visa_vector_db"
LOG_PATH = BASE_DIR / "logs" / "decision_logs.jsonl"

# Convert to string (important for some libs)
JSON_PATH = str(JSON_PATH)
VECTOR_DB_PATH = str(VECTOR_DB_PATH)
LOG_PATH = str(LOG_PATH)

# ==============================
# Model Settings
# ==============================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3

# ==============================
# API KEY HANDLING (BEST PRACTICE)
# ==============================
def get_secret(key, default=None):
    try:
        import streamlit as st
        return st.secrets.get(key, os.getenv(key, default))
    except:
        return os.getenv(key, default)
    
def get_google_api_key():
    return get_secret("GOOGLE_API_KEY")
