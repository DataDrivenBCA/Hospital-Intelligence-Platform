import streamlit as st
import pickle
import pandas as pd

with open('model_small.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Hospital Readmission Risk Predictor")
st.write("Enter patient details to predict readmission risk")

age = st.slider("Patient Age", 1, 100, 50)
length_of_stay = st.slider("Length of Stay (days)", 1, 30, 10)
billing_amount = st.number_input("Billing Amount ($)", min_value=1000, max_value=100000, value=25000)
medical_condition = st.selectbox("Medical Condition", ["Arthritis", "Asthma", "Cancer", "Diabetes", "Hypertension", "Obesity"])
admission_type = st.selectbox("Admission Type", ["Elective", "Emergency", "Urgent"])

if st.button("Predict Readmission Risk"):
    input_data = pd.DataFrame({
        'age': [age],
        'length_of_stay': [length_of_stay],
        'billing_amount': [billing_amount],
        'medical_condition_Arthritis': [1 if medical_condition == 'Arthritis' else 0],
        'medical_condition_Asthma': [1 if medical_condition == 'Asthma' else 0],
        'medical_condition_Cancer': [1 if medical_condition == 'Cancer' else 0],
        'medical_condition_Diabetes': [1 if medical_condition == 'Diabetes' else 0],
        'medical_condition_Hypertension': [1 if medical_condition == 'Hypertension' else 0],
        'medical_condition_Obesity': [1 if medical_condition == 'Obesity' else 0],
        'admission_type_Elective': [1 if admission_type == 'Elective' else 0],
        'admission_type_Emergency': [1 if admission_type == 'Emergency' else 0],
        'admission_type_Urgent': [1 if admission_type == 'Urgent' else 0]
    })

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.error(f"HIGH RISK — {round(probability*100, 1)}% probability of readmission")
    else:
        st.success(f"LOW RISK — {round(probability*100, 1)}% probability of readmission")
