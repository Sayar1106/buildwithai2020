import streamlit as st
from PIL import Image


def main():
    st.title("Team hotspot COVID-19 forecaster")
    st.write("This web-app will serve to forcast the number of COVID cases between July, 27, 2020 and August, 15, 2020. Coronavirus",
             "disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome",
             "coronavirus 2 (SARS-CoV-2). It was first identified in 2019 in Wuhan, China.")
    image = Image.open("assets/edwin-hooper-Q8m8cLkryeo-unsplash.jpg")
    image = image.resize((825, 550))
    st.image(image)
