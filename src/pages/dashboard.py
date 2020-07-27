import streamlit as st
from datetime import timedelta, datetime
from src.utils.fetch_url
from src.utils.load_data
import plotly.io as pio
import plotly.express as px
from plotly import graph_objs as go
import plotly


def main():
    st.title("Dashboard")
    pio.templates.default = "plotly_dark"
    date = datetime.today()
    DATA_URL = ""
    df = None
    while True:
        try:
            df = load_data(fetch_url(date))
        except:
            date = date - timedelta(days=1)
            continue
        break
