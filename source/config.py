import os

# ==========================
# BASE DIRECTORIES
# ==========================
# This ensures paths work both locally and in containers
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# ==========================
# JSON POLICY DATA
# ==========================
JSON_PATH = os.path.join(DATA_DIR, "policy_data.json")

# ==========================
# VECTOR DB / FAISS INDEX
# ==========================
# Folder containing index.faiss and index.pkl
VECTOR_DB_PATH = os.path.join(DATA_DIR, "faiss_index")

# ==========================
# EMBEDDING MODEL
# ==========================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # change as needed

# ==========================
# Retrieval Settings
# ==========================
TOP_K = 3  # number of top results to fetch

# ==========================
# LOGGING
# ==========================
LOG_PATH = os.path.join(BASE_DIR, "logs", "eligibility_logs.jsonl")

# ==========================
# GOOGLE API KEY
# ==========================
# Fetch from environment variables for security
def get_google_api_key():
    key = os.environ.get("GOOGLE_API_KEY")
    if not key:
        print("[WARN] GOOGLE_API_KEY not found in environment variables.")
    return key
