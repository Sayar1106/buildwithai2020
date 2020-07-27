import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
import plotly.express as px
import plotly.io as pio

def main():
   st.title("Forecaster")
   pio.templates.default = "plotly_dark"
   os.path
   path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Predictions'))
   states = [f.split(".")[0] for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

   state = st.sidebar.selectbox("Select the State", ["Overall"]+states)
   st.subheader(state)
   df = pd.read_csv(path + "/{}.csv".format(state), index_col=0, skiprows=[1,2,3,4], usecols=[0, 1])
   df["Confirmed"] = round(df["Confirmed"])
   if st.checkbox("Show raw data"):
       st.subheader('Raw data')
       st.write(df)
   fig = px.bar(x=df.index,
                y=df["Confirmed"],
                color=df.index,
                text=df["Confirmed"],
                color_discrete_sequence=px.colors.sequential.Reds)
   fig.update_xaxes(title="Date")
   fig.update_yaxes(title="Counts")
   fig.update_traces(textposition='outside',
                     texttemplate="%{text: .3s}",
                     hovertemplate=('<br>Count: %{y:,.2f}'
                                    '<br> Date: %{x}'))

   fig.update_layout(title="Forecasted values for {}".format(state),
                     width=900,
                     showlegend=False)
   st.plotly_chart(fig)
   


