
✈️ SwiftVisa AI – AI-Based Visa Eligibility Screening System

SwiftVisa AI is an end-to-end intelligent visa screening system that uses:

📚 Retrieval-Augmented Generation (RAG)
🧠 Large Language Models (LLM)
📊 Rule-based validation
🗂 Structured visa policy data

to provide accurate, explainable, and transparent visa eligibility decisions.

🚀 Project Objective

To build an AI system that:

Automates visa eligibility screening
Reduces manual verification effort
Provides explainable decision-making
Guides users with missing requirements


🔗 Project Link

🌐 Live App: https://your-app-link.streamlit.app



🏗️ System Architecture


Visa Policy Data
      ↓
Chunking & Embedding
      ↓
FAISS Vector DB
      ↓
User Input (Streamlit UI)
      ↓
Query Builder
      ↓
Retriever (Top-K Results)
      ↓
LLM + Rule Engine
      ↓
Eligibility Decision
      ↓
Logs + Admin Dashboard


📌 Milestones


🟢 Milestone 1 – Data Processing & Embedding

✔ Structured visa policy dataset
✔ Stored in data/clean/visa_policies.json
✔ Text chunking using RecursiveCharacterTextSplitter
✔ Generated embeddings (HuggingFace)
✔ Stored vectors in FAISS


🟢 Milestone 2 – Retrieval System (RAG)

✔ Built FAISS-based retriever
✔ Query generation from user profile
✔ Top-K semantic search
✔ Context-aware policy retrieval


🟢 Milestone 3 – AI Decision Engine

✔ LLM integration (Gemini)
✔ Hybrid decision system:

Rule-based validation
AI reasoning

✔ Outputs:

Decision (ELIGIBLE / REVIEW / NOT_ELIGIBLE)
Risk level
Confidence score


🟢 Milestone 4 – Application Layer & Monitoring

✔ Streamlit UI (app.py)
✔ Multi-step visa application flow
✔ AI chatbot (retrieval-based)
✔ Logging system (decision_logs.jsonl)
✔ Admin dashboard (log viewer)


swiftvisa-ai/
│
├── data/
│   └── clean/
│       └── visa_policies.json              # Structured visa policies dataset
│
├── logs/
│   └── decision_logs.jsonl                 # Application & decision logs
│
├── Output/
│   └── Visa_vector_db/                     # ⚠️ Auto-generated FAISS vector database
│       ├── index.faiss                     # FAISS index file
│       └── index.pkl                       # Metadata / mapping file
│
├── source/
│   ├── __init__.py
│   ├── app.py                              # Streamlit UI (deployment layer)
│   ├── build_vector.py                     # Chunking + embedding + FAISS creation
│   ├── config.py                           # Configuration (paths, constants)
│   ├── eligibility_prompt.py               # LLM prompt templates
│   ├── list_model.py                       # Model listing / selection
│   ├── llm_client.py                       # LLM integration (Gemini API)
│   ├── log_viewer.py                       # Admin dashboard (log viewer)
│   ├── ragpipeline.py                      # Core RAG pipeline logic
│   ├── retriever.py                        # FAISS retrieval system
│   ├── test_ragpipeline.py                 # RAG pipeline tests
│   └── test_retriever.py                   # Retriever tests
│
├── requirements.txt                        # Project dependencies
│
└── README.md


🧠 Core Components

🔹 Chunking & Embedding
Converts visa policies → vector format
Enables semantic search

🔹 FAISS Vector DB
Stores embeddings
Fast similarity search

🔹 Retriever
Finds relevant visa rules
Improves accuracy over keyword search

🔹 RAG Pipeline
Combines retrieval + LLM
Generates context-aware decisions

🔹 LLM Engine
Produces reasoning
Assigns risk & confidence

🔹 Logging System
Stores all applications
Enables monitoring & debugging


⚙️ Tech Stack

Frontend: Streamlit
Backend: Python
Vector DB: FAISS
Embeddings: Sentence Transformers
LLM: Gemini API
Storage: JSON / JSONL


▶️ Run the Project

pip install -r requirements.txt
streamlit run source/app.py


🔮 Future Enhancements


📎 Document upload & verification
🌍 Expand visa coverage
📊 Analytics dashboard
🔐 Authentication system
🧾 PDF report generation


👨‍💻 Author

Revan Kumar Battini


💡 Key Highlight

This project demonstrates a complete AI pipeline:

Data engineering (JSON → chunks → embeddings)
Vector search (FAISS)
Retrieval systems (RAG)
LLM reasoning
Explainable AI outputs
