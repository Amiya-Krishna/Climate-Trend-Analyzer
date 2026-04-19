import streamlit as st
import plotly.express as px
from src.data_loader import load_data
from src.preprocess import clean_data
from src.anomaly import detect_anomalies

st.title("📊 Climate Dashboard")

df = load_data("data/climate.csv")
df = clean_data(df)
df = detect_anomalies(df)

st.metric("Avg Temperature", round(df["Temperature"].mean(), 2))
st.metric("Max Temperature", round(df["Temperature"].max(), 2))

fig = px.line(df, x="Date", y="Temperature", title="Temperature Trend")
st.plotly_chart(fig, use_container_width=True)

st.subheader("⚠ Anomalies")
st.dataframe(df[df["anomaly"] == True])