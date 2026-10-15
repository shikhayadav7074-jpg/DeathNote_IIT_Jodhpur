# DeathNote_IIT_Jodhpur
# GlucoTwin - Digital Twin for Type 2 Diabetes Prediction
**Team Name:** Death Note
**College:** IIT Jodhpur
**Team Leader:** Yug Purush Balyan
**Team Member:** Shikha

### Problem Statement
India has 100M+ Type 2 Diabetes patients. Current care is reactive. We are building a proactive Digital Twin that fuses Static EHR + Dynamic wearable data to predict hyperglycemia 2 hours in advance.

### Architecture
Wearable (CGM, HR, Sleep) + Simulated EHR (Synthea) -> Data Fusion Layer -> LSTM Model -> Risk Prediction -> Doctor Dashboard with What-If Simulator

### Tech Stack
Python, Pandas, Scikit-learn, TensorFlow (LSTM), FastAPI, Streamlet, Synthea (Synthetic EHR), OhioT1DM Dataset

### Dataset Used (Sandbox Compliant)
1. EHR: Synthea generated / MIMIC-IV Demo (Anonymized)
2. Sensor: OhioT1DM Dataset (Open-source CGM + Heart Rate + Steps)

### How to Run
pip install -r requirements.txt
python generate_data.py
python train_model.py
streamlit run dashboard.py
License: MIT License - See LICENSE file for details.
