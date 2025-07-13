
```markdown
# 🤖 RAG Q&A Chatbot – Loan Approval Dataset

This is a Retrieval-Augmented Generation (RAG) chatbot that allows users to ask intelligent questions about a **Loan Approval Dataset**. It combines **vector-based document retrieval** with **Pandas analytics** and **generative AI models** (like Hugging Face’s `flan-t5`) to answer user queries.

---

## 📁 Project Structure

```

rag\_loan\_chatbot/
├── data/
│   └── Training Dataset.csv         # Source data (Kaggle)
├── embeddings/
│   └── faiss\_index.pkl              # Saved FAISS vector index
├── app.py                           # Streamlit app
├── retriever.py                     # Embedding + vector search logic
├── generator.py                     # Answer logic (Pandas + LLM)
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

````

---

## 🚀 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YashGunjal16/CSi-Assignments.git
cd CSi-Assignments/week7/rag_loan_chatbot
````

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🔍 Sample Questions You Can Ask

Here are a few example queries:

| # | Question                                                    |
| - | ----------------------------------------------------------- |
| 1 | How many applicants are self-employed?                      |
| 2 | Do married applicants get higher loan amounts?              |
| 3 | What is the average loan for graduates?                     |
| 4 | Are rural applicants more likely to get approved?           |
| 5 | How many dependents do approved applicants have on average? |

---

## 🧠 How It Works

* 🔎 **Retriever (`retriever.py`)**: Uses `sentence-transformers` to embed your question and retrieves relevant records using FAISS.
* 🧮 **Analyzer (`generator.py`)**:

  * If the question is analytical (e.g. count, mean), it runs Pandas logic.
  * Otherwise, it uses a lightweight LLM (like `flan-t5-base`) to generate a smart answer based on retrieved context.

---

## 📊 Dataset Used

* **Dataset**: [Loan Approval Prediction - Kaggle](https://www.kaggle.com/datasets/sonalisingh1411/loan-approval-prediction)
* **File**: `Training Dataset.csv` (already included in `/data` folder)

---

## 🖥️ Screenshot

> Example UI View

![RAG Chatbot Screenshot]<img src="https://github.com/YashGunjal16/CSi-Assignments/blob/main/week7/rag_loan_chatbot/demo.gif" width="700"/>


---

## 🧾 Requirements

Install dependencies from:

```
requirements.txt
```

Includes:

* `streamlit`
* `sentence-transformers`
* `faiss-cpu`
* `pandas`
* `transformers`
* `scikit-learn`

---

## 📌 Future Enhancements

* [ ] Enable user CSV upload
* [ ] Add charts for numeric answers
* [ ] Add support for other datasets
* [ ] Support for OpenAI / Claude / Gemini if API is available

---

## 🙌 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [Hugging Face Transformers](https://huggingface.co/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Kaggle Dataset](https://www.kaggle.com/datasets/sonalisingh1411/loan-approval-prediction)

---

## 📃 License

For educational use only. Dataset license per original Kaggle terms.

```

---

### ✅ How to use this:
- Just copy-paste into a file named `README.md` inside your `rag_loan_chatbot/` folder.
- Replace the image link in `![RAG Chatbot Screenshot]()` with a hosted image URL or remove it if unnecessary.

Let me know if you'd like me to generate a **GitHub badge**, **deployment badge**, or **add image hosting tips**.
```
