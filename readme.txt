# 🤖 DSA Copilot AI - Multi-Agent RAG Assistant

An AI-powered Data Structures & Algorithms assistant that leverages **Mistral AI**, **LangChain**, **Retrieval-Augmented Generation (RAG)**, and **ChromaDB** to solve DSA problems, explain code, generate interview questions, and provide personalized learning assistance.

---

## 🚀 Features

- 📚 Ask DSA and Competitive Programming questions
- 🔍 Retrieval-Augmented Generation (RAG) using custom PDFs
- 🤖 Multi-Agent architecture for intelligent task routing
- 💡 Step-by-step explanations and optimized solutions
- 👨‍💻 Java/Python code generation
- 📊 Time & Space Complexity analysis
- 📝 Generate new interview questions by topic
- 🎯 Hint generation without revealing the complete solution
- 🧠 Semantic search using HuggingFace embeddings
- 💬 Context-aware responses using Mistral AI

---

## 🏗️ Architecture

```
                User Query
                     │
                     ▼
            Query Classifier Agent
                     │
      ┌──────────────┼───────────────┐
      ▼              ▼               ▼
 RAG Agent     Hint Agent      Code Agent
      │                              │
      ▼                              ▼
 Question Generator Agent      Response Formatter
                     │
                     ▼
               Final Response
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| LLM | Mistral AI |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace Sentence Transformers |
| Document Loader | PyPDF |
| Environment | Python Dotenv |
| AI Technique | Retrieval-Augmented Generation (RAG) |

---

## 📂 Project Structure

```
dsa-copilot-ai/
│
├── data/
│   └── dsa_notes.pdf
│
├── db/
│
├── agents/
│   ├── classifier.py
│   ├── rag_agent.py
│   ├── hint_agent.py
│   ├── code_agent.py
│   └── question_generator.py
│
├── llm.py
├── prompt.py
├── ingest.py
├── rag.py
├── main.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/dsa-copilot-ai.git
```

Move into the project

```bash
cd dsa-copilot-ai
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```env
MISTRAL_API_KEY=YOUR_API_KEY
```

---

## 📥 Add Knowledge Base

Place your DSA PDFs inside

```
data/
```

Example:

```
data/
    Striver_SDE_Sheet.pdf
    Graphs.pdf
    DP_Notes.pdf
```

---

## 📚 Build Vector Database

```bash
python ingest.py
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 💬 Example Queries

### Solve DSA Problems

```
Solve Longest Increasing Subsequence
```

### Explain Code

```
Explain this Java code
```

### Generate Hints

```
Give hints for N Queens
```

### Generate Questions

```
Generate 5 medium-level Graph interview questions
```

```
Create hard Dynamic Programming problems
```

---

## 🧠 Multi-Agent Workflow

### Query Classifier

Determines user intent and routes requests to the appropriate agent.

### RAG Agent

Retrieves relevant knowledge from PDFs and generates context-aware answers.

### Hint Agent

Provides incremental hints without revealing the complete solution.

### Code Explanation Agent

Explains user-provided code with logic and complexity analysis.

### Question Generator Agent

Creates original DSA interview questions based on selected topics and difficulty.

---

## 📊 AI Pipeline

```
PDFs
   │
   ▼
Document Loader
   │
   ▼
Text Splitter
   │
   ▼
HuggingFace Embeddings
   │
   ▼
ChromaDB
   │
   ▼
Retriever
   │
   ▼
Mistral AI
   │
   ▼
Final Response
```

---



## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Aditya Zaware**

If you like this project, consider giving it a ⭐ on GitHub!