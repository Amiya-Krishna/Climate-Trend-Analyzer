import numpy as np
from config import TEMP_COLUMN, ANOMALY_THRESHOLD

def detect_anomalies(df):

    mean = df[TEMP_COLUMN].mean()
    std = df[TEMP_COLUMN].std()

    df["anomaly"] = np.abs(df[TEMP_COLUMN] - mean) > ANOMALY_THRESHOLD * std

    print("\n🚨 Detected Anomalies:")
    print(df[df["anomaly"] == True])

    return df