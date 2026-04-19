import matplotlib.pyplot as plt
import os

def analyze_trends(df):

    os.makedirs("outputs", exist_ok=True)

    df = df.sort_values("Date")

    # 📈 Raw Trend
    plt.figure(figsize=(10,5))
    plt.plot(df["Date"], df["Temperature"], label="Temperature")
    plt.title("Temperature Trend")
    plt.grid()
    plt.tight_layout()
    plt.savefig("outputs/raw_trend.png")
    plt.close()

    # 📉 Rolling Mean
    df["rolling_mean"] = df["Temperature"].rolling(12).mean()

    plt.figure(figsize=(10,5))
    plt.plot(df["Date"], df["rolling_mean"], color="red")
    plt.title("Smoothed Trend (12-month)")
    plt.grid()
    plt.tight_layout()
    plt.savefig("outputs/smoothed_trend.png")
    plt.close()

    return df