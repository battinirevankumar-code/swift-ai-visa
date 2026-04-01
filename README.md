# SwiftVisa AI – AI-Based Visa Eligibility Screening System

SwiftVisa AI is an end-to-end intelligent visa screening system that uses:

📚 Retrieval-Augmented Generation (RAG)  
🧠 Large Language Models (LLM)  
📊 Rule-based validation  
🗂 Structured visa policy data  

to provide accurate, explainable, and transparent visa eligibility decisions.

---

## 🚀 Project Objective

To build an AI system that:

- Automates visa eligibility screening  
- Reduces manual verification effort  
- Provides explainable decision-making  
- Guides users with missing requirements  

---

## 🔗 Project Link

🌐 Live App: https://your-app-link.streamlit.app  

---

## 📂 Project Structure

```
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
```


## 🧠 Core Components

### 🔹 Chunking & Embedding
Transforms raw visa policy documents into smaller, meaningful text chunks using intelligent splitting strategies (e.g., RecursiveCharacterTextSplitter).  
Each chunk is then converted into dense vector embeddings using pre-trained transformer models.

**Why it matters:**
- Improves retrieval accuracy  
- Handles large documents efficiently  
- Enables semantic understanding instead of keyword matching  

---

### 🔹 FAISS Vector DB
A high-performance vector database that stores embeddings and enables fast similarity search using nearest neighbor algorithms.

**Key features:**
- Optimized for large-scale vector storage  
- Supports fast Top-K similarity retrieval  
- Lightweight and efficient for local deployment  

---

### 🔹 Retriever
Responsible for fetching the most relevant visa policy chunks based on user input.

**How it works:**
- Converts user query into embeddings  
- Performs similarity search in FAISS  
- Returns Top-K most relevant policy contexts  

**Benefits:**
- Reduces irrelevant data passed to LLM  
- Improves response precision  
- Enables context-aware reasoning  

---

### 🔹 RAG Pipeline (Retrieval-Augmented Generation)
The core intelligence layer that combines retrieved context with LLM reasoning.

**Pipeline flow:**
1. User input → query generation  
2. Retrieve relevant policy chunks  
3. Inject context into LLM prompt  
4. Generate structured eligibility response  

**Why RAG:**
- Reduces hallucinations  
- Grounds responses in real policy data  
- Improves explainability  

---

### 🔹 LLM Engine
Handles natural language understanding and decision-making using Gemini API.

**Responsibilities:**
- Interpret user profile  
- Apply reasoning on retrieved policies  
- Generate structured outputs  

**Outputs include:**
- Eligibility decision (ELIGIBLE / REVIEW / NOT_ELIGIBLE)  
- Risk level (LOW / MEDIUM / HIGH)  
- Confidence score (%)  
- Justification for decision  

---

### 🔹 Rule-Based Validation Layer
A deterministic validation layer that enforces strict visa rules alongside AI reasoning.

**Examples:**
- Minimum work experience checks  
- Age or qualification constraints  
- Mandatory document validation  

**Purpose:**
- Ensures consistency and reliability  
- Prevents incorrect AI assumptions  
- Adds explainable rule enforcement  

---

### 🔹 Logging System
Captures every user interaction and system decision in structured format (`JSONL`).

**What is logged:**
- User profile input  
- Retrieved contexts  
- LLM responses  
- Final decision output  

**Benefits:**
- Debugging & error tracing  
- Monitoring system performance  
- Building admin dashboards  

---

### 🔹 Admin Dashboard (Log Viewer)
A monitoring interface built using Streamlit to analyze application logs.

**Features:**
- View all past decisions  
- Filter by eligibility status  
- Inspect detailed reasoning  
- Track system behavior over time  

---

### 🔹 Streamlit Application Layer
Provides an interactive UI for users to input visa details and receive decisions.

**Capabilities:**
- Multi-step application flow  
- Real-time AI responses  
- Integrated chatbot for queries  
- Clean and user-friendly interface  

---
## ⚙️ Tech Stack

- Frontend: Streamlit  
- Backend: Python  
- Vector DB: FAISS  
- Embeddings: Sentence Transformers  
- LLM: Gemini API  
- Storage: JSON / JSONL  

---

## ▶️ Run the Project

```bash
pip install -r requirements.txt
streamlit run source/app.py
```

## 🔮 Future Enhancements

- 📎 Document upload & verification
- 🌍 Expand visa coverage
- 📊 Analytics dashboard
- 🔐 Authentication system
- 🧾 PDF report generation

## 👨‍💻 Author

 Revan Kumar Battini

## 💡 Key Highlight

- This project demonstrates a complete AI pipeline:

- Data engineering (JSON → chunks → embeddings)
- Vector search (FAISS)
- Retrieval systems (RAG)
- LLM reasoning
- Explainable AI outputs
