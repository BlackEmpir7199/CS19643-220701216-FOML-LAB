import streamlit as st
import requests
import random
st.title("🕵️‍♂️ Fake Job Posting Detector")

st.markdown("Enter job posting details below to check if it might be fake:")

# Input fields
title = st.text_input("Job Title")
location = st.text_input("Location")
department = st.text_input("Department")
salary_range = st.text_input("Salary Range")
company_profile = st.text_area("Company Profile")
description = st.text_area("Job Description")
requirements = st.text_area("Requirements")
benefits = st.text_area("Benefits")
telecommuting = st.selectbox("Is it a remote job?", [0, 1])
has_company_logo = st.selectbox("Company logo present?", [0, 1])
has_questions = st.selectbox("Has application questions?", [0, 1])
employment_type = st.selectbox("Employment Type", ["", "Full-time", "Part-time", "Contract", "Temporary", "Other"])
required_experience = st.selectbox("Required Experience", ["", "Internship", "Entry level", "Mid-Senior level", "Director", "Executive"])
required_education = st.selectbox("Required Education", ["", "High School", "Associate", "Bachelor's", "Master's", "Doctorate"])
industry = st.text_input("Industry")
function = st.text_input("Function")

# Submit button
if st.button("Check Job Posting"):
    payload = {
        "title": title,
        "location": location,
        "department": department,
        "salary_range": salary_range,
        "company_profile": company_profile,
        "description": description,
        "requirements": requirements,
        "benefits": benefits,
        "telecommuting": telecommuting,
        "has_company_logo": has_company_logo,
        "has_questions": has_questions,
        "employment_type": employment_type,
        "required_experience": required_experience,
        "required_education": required_education,
        "industry": industry,
        "function": function
    }

    # Send to FastAPI
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        if(result['prediction']==1):
            st.error(f"🧠 Prediction: Fake")
        else:    
            st.success(f"🧠 Prediction: True")
        # probability_fake = result['probability_fake'];
        # st.info(f"📊 Probability of being True: {100-probability_fake:.2f}")
        # st.info(f"📊 Probability of being Fake: {probability_fake:.2f}")
    else:
        st.error("Something went wrong. Please try again.")

