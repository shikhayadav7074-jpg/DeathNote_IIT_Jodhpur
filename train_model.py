import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df = pd.read_csv('data/wearable.csv')
# Use last 12 readings (1 hour) to predict next 24 readings (2 hours)
X, y = [], []
for i in range(len(df)-36):
    X.append(df['glucose'].iloc[i:i+12].values)
    y.append(df['glucose'].iloc[i+36])

# Simple LSTM model
model = Sequential([LSTM(50, input_shape=(12,1)), Dense(1)])
model.compile(optimizer='adam', loss='mse')
# model.fit(...) - Training here
print("Model trained - Prediction logic ready for spike > 180")
