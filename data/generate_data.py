import pandas as pd
import numpy as np

np.random.seed(42)

# ================= DATE RANGE =================
dates = pd.date_range("2015-01-01", "2024-12-01", freq="MS")
n = len(dates)

# ================= SEASONALITY =================
months = dates.month

# Temperature seasonality (hot summers, cold winters)
seasonal_temp = 10 * np.sin(2 * np.pi * months / 12)

# Rainfall seasonality (monsoon effect simulation)
seasonal_rain = 40 * np.cos(2 * np.pi * months / 12)

# ================= DATA GENERATION =================
temperature = (
    25
    + seasonal_temp
    + np.random.normal(0, 2, n)
    + np.linspace(0, 2, n)   # global warming trend
)

rainfall = (
    100
    + seasonal_rain
    + np.random.normal(0, 10, n)
)

co2 = (
    400
    + np.linspace(0, 50, n)
    + np.random.normal(0, 5, n)
)

# ================= ADD ANOMALIES =================
anomaly_indices = np.random.choice(n, size=8, replace=False)
temperature[anomaly_indices] += np.random.normal(8, 2, 8)  # heatwaves

# ================= DATAFRAME =================
df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature,
    "Rainfall": np.abs(rainfall),  # avoid negatives
    "CO2": co2
})

# ================= SAVE =================
df.to_csv("data/climate.csv", index=False)

print("✅ Realistic Climate Dataset Generated Successfully!")