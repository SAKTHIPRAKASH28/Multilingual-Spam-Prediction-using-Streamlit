import streamlit as st
from streamlit_option_menu import option_menu
import predictPage
import about
st.set_page_config(layout="wide")

with st.sidebar:
    selected = option_menu(None, ["Predict", 'About'],
                           icons=['chat', 'info-circle'], menu_icon="list", default_index=0)

if selected == 'Predict':
    predictPage.page()

if selected == 'About':
    about.page()
