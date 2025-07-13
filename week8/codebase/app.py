# app.py
import streamlit as st
from retriever import retrieve_context, build_faiss_index
from generator import generate_answer
import os

st.set_page_config(page_title="RAG Q&A Chatbot", layout="wide")
st.title("🤖 RAG Q&A Chatbot - Loan Approval Dataset")

# Build index once
if not os.path.exists("embeddings/faiss_index.pkl"):
    with st.spinner("Indexing dataset..."):
        build_faiss_index()

query = st.text_input("💬 Ask a question about the loan dataset:")

if query:
    with st.spinner("🔍 Retrieving context and generating answer..."):
        context = "\n".join(retrieve_context(query))
        answer = generate_answer(query, context)
        st.markdown(f"### ✅ Answer:\n{answer}")
        st.markdown("### 📄 Retrieved Context:")
        st.code(context)
