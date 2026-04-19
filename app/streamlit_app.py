import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data
from src.preprocess import clean_data
from src.anomaly import detect_anomalies
from src.chatbot import ask_ai
from src.report_generator import generate_report

# ================= CONFIG =================
st.set_page_config(page_title="Climate AI SaaS", layout="wide")

st.title("🌍 Climate Intelligence Platform")

# ================= LOAD DATA =================
df = load_data("data/climate.csv")
df = clean_data(df)
df = detect_anomalies(df)

# ================= SAFETY CHECK =================
required_cols = ["Date", "Temperature", "anomaly"]

for col in required_cols:
    if col not in df.columns:
        st.error(f"Missing column: {col}")
        st.stop()

# ================= SIDEBAR =================
menu = st.sidebar.radio("Menu", ["Dashboard", "AI Chat"])

# ================= DASHBOARD =================
if menu == "Dashboard":

    st.subheader("📊 Climate Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Avg Temp", round(df["Temperature"].mean(), 2))
    col2.metric("Max Temp", round(df["Temperature"].max(), 2))
    col3.metric("Anomalies", int(df["anomaly"].sum()))

    fig = px.line(df, x="Date", y="Temperature", title="Temperature Trend")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("⚠ Anomalies Detected")

    st.dataframe(df[df["anomaly"] == True])

    if st.button("📄 Generate Report"):

        path = generate_report(df)

        st.success("Report generated successfully!")

        with open(path, "rb") as file:
            st.download_button(
                label="⬇ Download Climate Report",
                data=file,
                file_name="climate_report.pdf",
                mime="application/pdf"
            )

# ================= AI CHAT =================
elif menu == "AI Chat":

    st.subheader("🤖 Climate AI Assistant")

    q = st.text_input("Ask anything about climate data")

    if q:
        response = ask_ai(q, df)
        st.write(response)