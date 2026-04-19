from src.data_loader import load_data
from src.analytics_engine import analyze_trends
from src.anomaly import detect_anomalies
from src.forecast_engine import forecast_temperature
from src.report_generator import generate_pdf

DATA_PATH = "data/climate.csv"

def main():

    print("\n🌍 SaaS Climate Dashboard Started")

    df = load_data(DATA_PATH)

    df = analyze_trends(df)

    anomalies = detect_anomalies(df)

    forecast = forecast_temperature(df)

    pdf_path = generate_pdf(df, anomalies, forecast)

    print("\n✅ PDF Generated:", pdf_path)

if __name__ == "__main__":
    main()