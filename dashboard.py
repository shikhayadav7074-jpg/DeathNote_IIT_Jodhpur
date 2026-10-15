import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="GlucoTwin - IIT Jodhpur", layout="wide")

# --- Header ---
st.title("🩺 GlucoTwin - Digital Twin Dashboard")
st.markdown("**Team Death Note | IIT Jodhpur | Team Leader: Yug Purush Balyan**")
st.divider()

# --- Load Data (Mock Data for Demo) ---
# Agar tumhari wearable.csv nahi hai to ye fake data se chal jayega
try:
    df = pd.read_csv('data/wearable.csv')
except:
    time = pd.date_range('2026-10-15 06:00', periods=200, freq='5min')
    glucose = 110 + 40*np.sin(np.arange(200)/20) + np.random.randn(200)*5
    hr = 78 + np.random.randn(200)*3
    df = pd.DataFrame({'time': time, 'glucose': glucose, 'heart_rate': hr})

# --- Sidebar - Static EHR (Digital Twin Profile) ---
st.sidebar.header("Patient Digital Twin Profile (EHR)")
st.sidebar.metric("Patient ID", "P001 - Male, 45Y")
st.sidebar.metric("BMI", "28.5 (Overweight)")
st.sidebar.metric("HbA1c", "8.2% (High)")
st.sidebar.metric("Diabetic Since", "5 Years")
st.sidebar.metric("Family History", "Yes")

# --- Main Dashboard - 3 Columns ---
col1, col2, col3 = st.columns(3)
current_glucose = df['glucose'].iloc[-1]
predicted_glucose = current_glucose + 35 # Mock prediction

col1.metric("Current Glucose", f"{current_glucose:.1f} mg/dL", "+2.1")
col2.metric("Predicted (in 2 Hrs)", f"{predicted_glucose:.1f} mg/dL", "- High Risk", delta_color="inverse")
col3.metric("Heart Rate (Live)", f"{df['heart_rate'].iloc[-1]:.0f} bpm")

# --- Risk Alert Logic ---
if predicted_glucose > 180:
    st.error("🚨 **ALERT: High Risk of Hyperglycemia in 90-120 mins!** Suggested Action: 15 min walk + 500ml water. Inform Doctor.")
elif predicted_glucose > 150:
    st.warning("⚠️ **Medium Risk:** Glucose trending up. Avoid carbs in next meal.")
else:
    st.success("✅ **Low Risk:** Patient stable.")

# --- Graphs ---
st.subheader("Live Data Fusion - Last 12 Hours")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['time'], y=df['glucose'], mode='lines', name='Glucose (CGM)', line=dict(color='red')))
fig.add_trace(go.Scatter(x=df['time'], y=df['heart_rate'], mode='lines', name='Heart Rate', yaxis='y2', line=dict(color='blue')))
fig.update_layout(yaxis=dict(title="Glucose mg/dL"), yaxis2=dict(title="Heart Rate bpm", overlaying="y", side="right"))
st.plotly_chart(fig, use_container_width=True)

# --- What-If Simulator (Digital Twin ka Jadoo) ---
st.divider()
st.subheader("🔬 Digital Twin Simulator - What-If Analysis")
st.write("Doctor can simulate: What happens if patient eats now?")
carbs = st.slider("Simulate Carb Intake (grams)", 0, 100, 20)
if st.button("Run Simulation"):
    simulated_spike = predicted_glucose + (carbs * 0.8)
    st.write(f"If patient eats {carbs}g carbs now, predicted glucose in 2 hours will be: **{simulated_spike:.1f} mg/dL**")
    st.progress(min(int(simulated_spike/250*100), 100))

st.caption("Data Source: Synthetic EHR (Synthea) + Open-source Wearable (OhioT1DM pattern) | Compliant with DPDP Act")
