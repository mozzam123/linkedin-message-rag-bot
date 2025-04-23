# Simple RAG Bot for LinkedIn Messages

A simple yet powerful Retrieval-Augmented Generation (RAG) pipeline built **from scratch** without LangChain, using your own **LinkedIn Messages** exported from a CSV file.

---

# 🔹 Project Overview

| Stack | Tools |
|:---|:---|
| Programming Language | Python |
| Embeddings | `sentence-transformers` (all-MiniLM) |
| Vector Store | FAISS |
| LLM Completion | Groq API (LLaMA3 70B) |
| Environment | `.env` for API keys |


This bot allows you to **ask questions** about your past LinkedIn conversations and get **smart answers** generated based on **retrieved relevant messages**.

---

# 📚 How It Works

```bash
CSV Messages (.csv)
   ⬇️
MessageLoader
   ⬇️
Embedder (sentence-transformers)
   ⬇️
VectorStore (FAISS)
   ⬇️
Retriever (Top-k Relevant Messages)
   ⬇️
Generator (Groq API - LLaMA3)
   ⬇️
Final Answer
```

---

# 📂 Folder Structure

```bash
simple_rag_linkedin_bot/
|
├── data/
│   └── messages.csv
├── src/
│   ├── loader.py         # Load CSV messages
│   ├── embedder.py       # Create embeddings
│   ├── vectorstore.py    # FAISS vector database
│   ├── retriever.py      # Retrieve top relevant messages
│   ├── generator.py      # Generate answers using Groq API
│   └── app.py            # Main application runner
├── .env                  # Environment variables
├── requirements.txt
└── README.md             # Project Documentation
```

---

# 🔹 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/simple-rag-linkedin-bot.git
cd simple-rag-linkedin-bot
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Groq API Key

Create a `.env` file:
```bash
GROQ_API_KEY=your-groq-api-key-here
```

### 5. Add your exported messages file

Place your LinkedIn messages CSV in the `data/` folder as `messages.csv`.

### 6. Run the application
```bash
python src/app.py
```

---

# 🌐 Example Usage

```bash
✅ Loaded 500 messages.
✅ Embedded 500 messages.
✅ Vector store created.

🧙‍♂️ RAG Bot is ready! Ask questions about your LinkedIn messages.

❓ Enter your question: Did I talk to anyone about salary?
🔍 Retrieved 5 relevant messages.

💬 Answer: Yes, you discussed salary with Palash Dhavle mentioning a 50k monthly offer.
```

---

# 📑 Requirements

- Python 3.8+
- Packages listed in `requirements.txt`:
  - `pandas`
  - `faiss-cpu`
  - `sentence-transformers`
  - `groq`
  - `python-dotenv`

---

# ✨ Future Improvements

- [ ] Build a FastAPI or Gradio frontend
- [ ] Add conversation summarization feature
- [ ] Support multi-turn RAG (follow-up questions)
- [ ] Store FAISS index persistently

---


