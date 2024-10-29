import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('heart_disease_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

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
    .black-text {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Heart Disease Prediction App")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Heart Disease Prediction", "Cardiologists", "Heart Disease Information"])

# Tab 1: Heart Disease Prediction
with tab1:
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

# Tab 2: Cardiologists
with tab2:
    st.header("Suggested Cardiologists")
    cardiologists = [
        {
            "Name": "Dr. Ashok Seth",
            "Speciality": "Interventional Cardiologist",
            "Qualification": "MBBS, MD, DM, MRCP",
            "Experience": "38+ Years",
            "Location": "New Delhi",
            "Hospital": "Fortis Escorts Hospital, New Delhi"
        },
        {
            "Name": "Dr. T S Kler",
            "Speciality": "Interventional Cardiologist",
            "Qualification": "MBBS, MD, DM, Fellow of Royal College of Physicians (FRCP), UK and Fellow of American College of Cardiology (FACC)",
            "Experience": "30+ Years",
            "Location": "Gurgaon",
            "Hospital": "FMRI, Gurgaon"
        },
        {
            "Name": "Dr. Subhash Chandra",
            "Speciality": "Interventional Cardiologist",
            "Qualification": "MBBS, MD, DM, DNB, United States Medical Licensing Examination (USA) & PDF (Brussels, Belgium)",
            "Experience": "39+ Years",
            "Location": "Delhi",
            "Hospital": "BLK Hospital, Delhi"
        },
        {
            "Name": "Dr. (Col.) Manjinder Singh Sandhu",
            "Speciality": "Interventional Cardiologist",
            "Qualification": "MBBS, MD, DM, DNB, Fellowship- American College of Cardiology",
            "Experience": "27+ Years",
            "Location": "Gurgaon",
            "Hospital": "Artemis Hospital, Gurgaon"
        },
        {
            "Name": "Dr. Aparna Jaswal",
            "Speciality": "Interventional Cardiologist",
            "Qualification": "MBBS, MD, DNB, Training, Cardiac Electrophysiology at St. Luke's Hospital in Milwaukee, USA",
            "Experience": "25+ Years",
            "Location": "Delhi",
            "Hospital": "Fortis Escorts Hospital, Delhi"
        }
    ]
    
    for doctor in cardiologists:
        st.subheader(doctor["Name"])
        st.markdown(f"<span class='black-text'>**Speciality:** {doctor['Speciality']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='black-text'>**Qualification:** {doctor['Qualification']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='black-text'>**Experience:** {doctor['Experience']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='black-text'>**Location:** {doctor['Location']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='black-text'>**Hospital:** {doctor['Hospital']}</span>", unsafe_allow_html=True)
        st.write("---")

# Tab 3: Heart Disease Information
with tab3:
    st.header("Heart Disease Information")
    st.markdown("""
    <span class='black-text'>
    Heart disease describes a range of conditions that affect the heart. 
    Heart disease includes:
    
    - Blood vessel disease, such as coronary artery disease.
    - Irregular heartbeats, called arrhythmias.
    - Heart conditions that you're born with, called congenital heart defects.
    - Disease of the heart muscle.
    
    **Heart disease symptoms caused by irregular heartbeats:**
    
    - Chest pain or discomfort.
    - Dizziness.
    - Fainting or almost fainting.
    - Fluttering in the chest.
    - Lightheadedness.
    - Racing heartbeat.
    - Shortness of breath.
    - Slow heartbeat.
    
    **Heart disease symptoms caused by congenital heart defects:**
    
    - Blue or gray skin.
    - Swelling in the legs, belly area, or areas around the eyes.
    - In an infant, shortness of breath during feedings, leading to poor weight gain.
    
    **Heart disease symptoms caused by diseased heart muscle (cardiomyopathy):**
    
    - Dizziness, lightheadedness, and fainting.
    - Fatigue.
    - Feeling short of breath during activity or at rest.
    
    **Heart disease symptoms caused by heart valve disease:**
    
    - Chest pain.
    - Fainting or almost fainting.
    - Fatigue.
    - Irregular heartbeats.
    
    **When to see a doctor:**
    
    - Get emergency medical help if you have these heart disease symptoms:
      - Chest pain.
      - Shortness of breath.
      - Fainting.
      
    Always call 911 or your local emergency number if you think you might be having a heart attack.
    
    **Prevention and Treatment:**
    Many forms of heart disease can be prevented or treated with healthy lifestyle choices.
    </span>
    """, unsafe_allow_html=True)
