# streamlit_app.py
import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🚢 Titanic Survival Predictor")

st.markdown("""
Enter passenger details to check if they would have survived the Titanic disaster.
""")

# User inputs
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.radio("Sex", ["male", "female"])
age = st.slider("Age", 0, 80, 30)
fare = st.slider("Fare Paid", 0, 500, 50)

# Convert inputs
sex_encoded = 0 if sex == "male" else 1
features = np.array([[pclass, sex_encoded, age, fare]])
features_scaled = scaler.transform(features)

# Prediction
if st.button("Predict Survival"):
    pred = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]

    st.subheader("Prediction Result:")
    if pred == 1:
        st.success(f"The passenger **would have survived**! (Probability: {prob:.2f})")
    else:
        st.error(f"The passenger **would not have survived**. (Probability: {prob:.2f})")
