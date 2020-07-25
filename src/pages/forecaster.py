import streamlit as st
from datetime import datetime, timedelta

def main():
   st.title("Forecaster")
   start_date = datetime(2020, 7, 27)
   st.sidebar.selectbox("Start Date", [start_date.date() + timedelta(days=x) for x in range(90)])
   st.sidebar.selectbox("End Date", [start_date.date() + timedelta(days=x) for x in range(90)])
