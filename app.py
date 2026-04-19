import streamlit as st
from src.data_loader import load_data
from src.analytics_engine import analyze_trends
from src.anomaly import detect_anomalies
from src.forecast_engine import forecast_temperature
from src.report_generator import generate_pdf

st.title("🌍 Climate SaaS Dashboard")

file = st.file_uploader("Upload CSV")

if file:

    df = load_data(file)

    df = analyze_trends(df)

    anomalies = detect_anomalies(df)

    forecast = forecast_temperature(df)

    pdf = generate_pdf(df, anomalies, forecast)

    st.success("Report Generated!")

    with open(pdf, "rb") as f:
        st.download_button("Download PDF Report", f, file_name="climate_report.pdf")