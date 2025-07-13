# generator.py
import pandas as pd
from transformers import pipeline

# Load model once
qa_pipeline = pipeline("text-generation", model="google/flan-t5-base")

# Load dataset
df = pd.read_csv("data/Training Dataset.csv")
df.fillna("Unknown", inplace=True)

def generate_answer(query, context):
    query_lower = query.lower()

    # Rule 1: Self-employed count
    if "self-employed" in query_lower or "self employed" in query_lower:
        count = df[df["Self_Employed"] == "Yes"].shape[0]
        return f"✅ There are **{count}** self-employed applicants in the dataset."

    # Rule 2: Average loan for married/unmarried
    if "married" in query_lower and "loan" in query_lower:
        married_avg = pd.to_numeric(df[df["Married"] == "Yes"]["LoanAmount"], errors="coerce").mean()

        unmarried_avg = pd.to_numeric(df[df["Married"] == "No"]["LoanAmount"], errors="coerce").mean()

        return (
            f"✅ On average, married applicants get higher loan amounts.\n\n"
            f"🔹 Married Avg Loan: ₹{married_avg:.2f}\n"
            f"🔹 Unmarried Avg Loan: ₹{unmarried_avg:.2f}"
        )

    # Rule 3: Education vs Loan Amount
    if "graduate" in query_lower or "education" in query_lower:
        grad_avg = df[df["Education"] == "Graduate"]["LoanAmount"].mean()
        non_grad_avg = df[df["Education"] == "Not Graduate"]["LoanAmount"].mean()
        return (
            f"📘 Graduate vs Non-Graduate Average Loan:\n\n"
            f"🔹 Graduate: ₹{grad_avg:.2f}\n"
            f"🔹 Not Graduate: ₹{non_grad_avg:.2f}"
        )

    # Fallback → use LLM
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    return qa_pipeline(prompt, max_new_tokens=100)[0]['generated_text']
