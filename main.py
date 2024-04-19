import streamlit as st
from streamlit_option_menu import option_menu
import predictPage
import about
st.set_page_config(layout="wide")
st.markdown(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <script>

      (adsbygoogle = window.adsbygoogle || []).push({
        google_ad_client: "ca-pub-1000196417768821",
        enable_page_level_ads: true
      });
    </script>
    """,
    unsafe_allow_html=True
)
with st.sidebar:
    selected = option_menu(None, ["Predict", 'About'],
                           icons=['chat', 'info-circle'], menu_icon="list", default_index=0)

if selected == 'Predict':
    predictPage.page()

if selected == 'About':
    about.page()
