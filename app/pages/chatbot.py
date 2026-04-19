import streamlit as st
from src.data_loader import load_data
import sys
import os

def setup_project_path():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if BASE_DIR not in sys.path:
        sys.path.insert(0, BASE_DIR)

st.title("🤖 Climate AI Assistant")

df = load_data("data/climate.csv")

q = st.text_input("Ask about climate trends")

if q:

    q = q.lower()

    if "temperature" in q:
        st.write(f"Avg Temperature: {df['Temperature'].mean():.2f}")

    elif "co2" in q:
        st.write("CO2 is increasing trend in dataset 📈")

    elif "rain" in q:
        st.write("Rainfall shows seasonal variation 🌧")

    else:
        st.write("I can answer about temperature, CO2, rainfall.")