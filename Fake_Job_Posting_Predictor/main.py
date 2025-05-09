from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import random
import numpy as np

# Helper function to convert NumPy types to Python native types
def convert_numpy_types(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {key: convert_numpy_types(value) for key, value in obj.items()}
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return [convert_numpy_types(item) for item in obj]
    else:
        return obj

# Load model
model = joblib.load("fake_job_detector (1).pkl")

app = FastAPI(title="Fake Job Detection API")

class JobPosting(BaseModel):
    title: str
    location: str
    department: str
    salary_range: str
    company_profile: str
    description: str
    requirements: str
    benefits: str
    telecommuting: int
    has_company_logo: int
    has_questions: int
    employment_type: str
    required_experience: str
    required_education: str
    industry: str
    function: str

class PredictionResponse(BaseModel):
    prediction: int
    probability_fake: float

@app.post("/predict", response_model=PredictionResponse)
def predict_job(posting: JobPosting):
    # Convert to DataFrame
    data = pd.DataFrame([posting.dict()])

    # Feature engineering (match model training)
    data['text'] = data['title'] + " " + data['company_profile'] + " " + data['description'] + " " + data['requirements'] + " " + data['benefits']
    data['title_length'] = data['title'].apply(len)
    data['num_links'] = data['description'].str.count("http|www")
    data['suspicious_words'] = data['description'].str.contains("limited positions|urgent|quick money|click here|guaranteed", case=False).astype(int)

    # Predict
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    
    # Convert NumPy types to Python native types
    prediction = convert_numpy_types(prediction)
    probability = convert_numpy_types(probability)
    

    return {
        "prediction": prediction,  # Fixed typo in key name
        "probability_fake": float(probability)
    }