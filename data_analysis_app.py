import sys
import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import operator as op
from itertools import chain
from PIL import Image
import snowflake.connector


image_s = Image.open('logo_s.png')
image = Image.open('logo.png')
#st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(
     page_title="Hakkoda data analysis tool",
     page_icon=image_s,
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://hakkoda.io/contact/',
         'About': "This is an app powered by Hakkoda for Data Analysis in Python and Streamlit"
     }
)

def get_data():
    return df

def show_data():
    col1, col2, col3= st.columns(3)
    with col2:
        st.image(image, caption='Empowering data-driven organizations', width=400)
    st.title("Diploma Data Analysis",)
    st.caption("Powered by Hakkoda for Data Analysis with Python | Made with Streamlit")
    st.write('El objetivo de esta demo es mostrar una conexión entre snowflake y una aplicación para analisis de datos hecha en python con la libreria streamlit')




if __name__=="__main__":
    show_data()