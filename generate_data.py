import pandas as pd
import numpy as np

# Static EHR - Synthea style
ehr_data = {
    'patient_id': ['P001'], 'age': [45], 'bmi': [28.5],
    'hba1c': [8.2], 'family_history': [1], 'years_diabetic': [5]
}

# Dynamic Wearable - 7 days, every 5 mins
time = pd.date_range('2026-10-01', periods=2000, freq='5min')
glucose = 120 + 30*np.sin(np.arange(2000)/100) + np.random.randn(2000)*5
hr = 75 + np.random.randn(2000)*3
steps = np.random.randint(0,100,2000)

df = pd.DataFrame({'time': time, 'glucose': glucose, 'heart_rate': hr, 'steps': steps})
df.to_csv('data/wearable.csv', index=False)
print("Data Generated: data/wearable.csv")
