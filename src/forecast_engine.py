import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from config import FORECAST_STEPS

def forecast_temperature(df):

    df = df.copy()
    df["time_index"] = np.arange(len(df))
    
    X = df[["time_index"]]
    y = df["Temperature"]

    model = LinearRegression()

    # ✅ FIX HERE
    model.fit(X.values, y.values)

    future_index = np.arange(len(df), len(df) + FORECAST_STEPS).reshape(-1, 1)
    forecast = model.predict(future_index)

    # ✅ FIX: pandas is now available here
    future_dates = pd.date_range(
        start=df["Date"].iloc[-1],
        periods=FORECAST_STEPS + 1,
        freq="MS"
    )[1:]

    return pd.DataFrame({
        "Date": future_dates,
        "Forecast_Temperature": forecast
    })