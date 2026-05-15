import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("heart_model.pkl", "rb"))

st.title("❤️ Heart Disease Prediction App")

age = st.number_input("Age")
sex = st.number_input("Sex (1=Male, 0=Female)")
cp = st.number_input("Chest Pain Type")
trestbps = st.number_input("Resting BP")
chol = st.number_input("Cholesterol")
fbs = st.number_input("Fasting Blood Sugar")
restecg = st.number_input("ECG")
thalach = st.number_input("Max Heart Rate")
exang = st.number_input("Exercise Angina")
oldpeak = st.number_input("Oldpeak")
slope = st.number_input("Slope")
ca = st.number_input("CA")
thal = st.number_input("Thal")

input_data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,
                        thalach,exang,oldpeak,slope,ca,thal]])

if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Risk of Heart Disease")
    else:
        st.success("✅ Healthy Heart")