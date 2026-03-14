import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("fraud_model.pkl", "rb"))

st.title("Fraud Detection App")

# Example input fields
amount = st.number_input("Transaction Amount")
oldbalanceOrg = st.number_input("Old Balance Origin")
newbalanceOrig = st.number_input("New Balance Origin")

if st.button("Predict"):
    input_data = np.array([[amount, oldbalanceOrg, newbalanceOrig]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Fraud Transaction")
    else:
        st.success("Not Fraud")
