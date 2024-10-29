import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('heart_disease_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("Heart Disease Prediction")

# Add CSS for background image and style adjustments
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.postimg.cc/1RTn8bYg/istockphoto-625147262-612x612.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;  /* Adjust text color for readability */
    }
    .stButton > button {
        background-color: #FF5722; /* Button color */
        color: white; /* Button text color */
        font-size: 16px;
    }
    .stTextInput, .stNumberInput, .stSelectbox {
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
        color: black; /* Input text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input form
age = st.number_input("Age", min_value=0, max_value=120)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3])
trtbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0.0)
chol = st.number_input("Cholesterol (mg/dl)", min_value=0.0)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1])
restecg = st.selectbox("Resting Electrocardiographic Results", options=[0, 1, 2])
thalachh = st.number_input("Maximum Heart Rate Achieved", min_value=0.0)
exng = st.selectbox("Exercise Induced Angina", options=[0, 1])
oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=0.0)
slp = st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1, 2])
caa = st.selectbox("Number of Major Vessels (0-3) Colored by Fluoroscopy", options=[0, 1, 2, 3])
thall = st.selectbox("Thalassemia", options=[0, 1, 2, 3])

# Prediction button
if st.button("Predict"):
    features = np.array([
        age,
        sex,
        cp,
        trtbps,
        chol,
        fbs,
        restecg,
        thalachh,
        exng,
        oldpeak,
        slp,
        caa,
        thall
    ]).reshape(1, -1)

    # Make the prediction
    prediction = model.predict(features)[0]

    # Display prediction result
    if prediction == 1:
        st.warning("You have heart disease. Please consult your doctor.")
    else:
        st.success("You have no heart disease.")

    # Display input values
    st.write("### Input values:")
    input_data = {
        "Age": age,
        "Sex": "Female" if sex == 0 else "Male",
        "Chest Pain Type": cp,
        "Resting BP": trtbps,
        "Cholesterol": chol,
        "Fasting Blood Sugar": fbs,
        "Resting ECG": restecg,
        "Max Heart Rate": thalachh,
        "Exercise Induced Angina": exng,
        "Oldpeak": oldpeak,
        "Slope": slp,
        "Caa": caa,
        "Thall": thall
    }
    st.write(input_data)
