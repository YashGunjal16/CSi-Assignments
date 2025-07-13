# retriever.py
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

def build_faiss_index(csv_path="data/Training Dataset.csv", save_path="embeddings/faiss_index.pkl"):
    df = pd.read_csv(csv_path)
    df.fillna("Unknown", inplace=True)
    texts = df.apply(lambda row: ' | '.join([str(x) for x in row.values]), axis=1).tolist()

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    with open(save_path, "wb") as f:
        pickle.dump((index, texts), f)

def retrieve_context(query, top_k=3):
    with open("embeddings/faiss_index.pkl", "rb") as f:
        index, texts = pickle.load(f)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)
    return [texts[i] for i in I[0]]
