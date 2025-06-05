
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load trained model and scaler
model = load_model("mlp_financial_inclusion_model.keras")
scaler = joblib.load("scaler.pkl")
selected_features = joblib.load("selected_features.pkl")  # List of selected input features

st.title("📊 Financial Inclusion Prediction")
st.subheader("Will this rural youth be financially included?")

# User input
user_inputs = {}
for feature in selected_features:
    if feature == "Income_Bracket":
        income_option = st.selectbox("Income Bracket", ["Non", "Low", "Medium"])
        user_inputs[feature] = income_option
    elif "Age" in feature or "Size" in feature:
        user_inputs[feature] = st.number_input(f"{feature}", min_value=0.0, step=1.0)
    else:
        user_inputs[feature] = st.selectbox(f"{feature}", ["No", "Yes"])

# Prepare input data
input_data = []
for feature in selected_features:
    val = user_inputs[feature]
    if feature == "Income_Bracket":
        mapped_val = {"Non": 0, "Low": 1, "Medium": 2}.get(val, 0)
        input_data.append(mapped_val)
    elif isinstance(val, str):
        input_data.append(1 if val == "Yes" else 0)
    else:
        input_data.append(val)

input_df = pd.DataFrame([input_data], columns=selected_features)

# Scale the input
input_scaled = scaler.transform(input_df)

# Predict probability
prob = model.predict(input_scaled)[0][0]
predicted_class = "Financially Included" if prob >= 0.5 else "Financially Excluded"

# Display results
st.markdown(f"### Prediction: **{predicted_class}**")
st.progress(float(prob))
st.markdown(f"**Probability of Financial Inclusion:** {prob:.2%}")
