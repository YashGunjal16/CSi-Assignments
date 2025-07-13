# 🤖 RAG Q&A Chatbot – Loan Approval Dataset

This project implements a **Retrieval-Augmented Generation (RAG)** based chatbot that answers natural language questions on a loan approval dataset. It intelligently retrieves relevant data and either uses a **generative LLM (Flan-T5)** or **Pandas-based analytics** to respond.

![App Screenshot](https://user-images.githubusercontent.com/00000000/demo.png) <!-- Replace with actual screenshot if public -->

---

## 📌 Features

- 🔎 **Semantic Search** using sentence embeddings + FAISS
- 🧠 **Hybrid Answering Engine**:
  - 📊 Uses **Pandas** for smart analytics (averages, counts, comparisons)
  - 🧬 Uses **LLMs** for unstructured context-based answers
- 🧾 **Interactive Streamlit UI**
- 📁 Upload your own dataset (optional extension)

---

## 🗂️ Project Structure

rag_loan_chatbot/
├── data/
│ └── Training Dataset.csv # Source data (Kaggle)
├── embeddings/
│ └── faiss_index.pkl # Saved FAISS vector index
├── app.py # Streamlit app
├── retriever.py # Embedding + vector search logic
├── generator.py # Answer logic (Pandas + LLM)
├── requirements.txt # Python dependencies
└── README.md # You're here

yaml
Copy
Edit

---

## 🚀 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YashGunjal16/CSi-Assignments.git
cd CSi-Assignments/week7/rag_loan_chatbot
2. Create virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # On Windows
# source venv/bin/activate  # On Mac/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
streamlit run app.py
🔍 Sample Questions You Can Ask
Question	Answer Engine
How many self-employed applicants are there?	🧮 Pandas
Do married applicants get higher loan amounts?	🧮 Pandas
What is the average loan for graduates vs non-graduates?	🧮 Pandas
What factors affect loan approval?	💬 LLM
Are applicants from rural areas more likely to be approved?	💬 LLM

📊 Dataset
Source: Loan Approval Dataset – Kaggle

Used for educational and prototyping purposes only.

🤝 Credits
SentenceTransformers

FAISS (Facebook AI Similarity Search)

HuggingFace Transformers

Streamlit

Dataset by: Sonali Singh (Kaggle)

📌 Future Enhancements
 User-uploadable CSV support

 Data visualizations in responses

 Multilingual question answering

 Switchable LLM (Gemini, GPT, Claude, etc.)

📸 UI Preview
<img src="https://github.com/YashGunjal16/CSi-Assignments/blob/main/week7/rag_loan_chatbot/demo.gif" width="700"/>
💡 License
This project is built for educational use. Please check the dataset’s original license before redistribution.

yaml
Copy
Edit

---

Let me know if you want:
- A **live badge** or deploy link section
- **Deployment-ready zip**
- Auto-push to GitHub

Ready to go 🎯
