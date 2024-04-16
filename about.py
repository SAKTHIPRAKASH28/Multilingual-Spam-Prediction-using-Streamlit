import streamlit as st
import pandas as pd


def sidebar_bg():

    st.markdown(
        f"""
       <style>
       [data-testid="stSidebar"] > div:first-child {{
           background-color:grey;
           );
       }}
       </style>
       """,
        unsafe_allow_html=True,
    )


def page():
    st.title("_About_")
    st.header("_Multilingual :red[spam] prediction:_", divider='red')
    st.markdown(
        f"**_<p style='font-size:20px;'>An API built with :red[FastAPI] that utilizes a machine learning model to predict whether a given message is :red[spam] or not.</p>_**", unsafe_allow_html=True)
    st.header("_Languages Supported_", divider="red")
    st.markdown("""
    <ul>
        <li>Tamil</li>
        <li>English</li>
        <li>Malayalam</li>
        <li>Kannada</li>
        <li>Telugu</li>
    </ul>
    """, unsafe_allow_html=True)
    st.header("_Usage_", divider="red")
    st.markdown(
        f"**_<p style='font-size:17px;'>:red[NOTE] : API may experience intermittent periods of downtime, as it is hosted on Render, kindly wait for the instance to come live before requesting.</p>_**", unsafe_allow_html=True)

    code = '''import requests
    url = 'https://sms-spam-prediction.onrender.com/predict'


    def req(message):
        response = requests.get(url, params={"message": message})
        return response.json()["prediction"]'''
    st.code(code, language='python')
    st.header("_Model Details_", divider="red")
    st.markdown(f"**_<p style='font-size:17px;'> :red[Random Forest Classifier], a robust machine learning algorithm known for its effectiveness in text classification tasks was used. The model was trained on a comprehensive :red[multilingual spam collection dataset], publicly available on the :red[IEEE Dataport]. This dataset encompasses a variety of spam and non-spam messages across multiple languages, allowing the model to generalize well and identify spam messages regardless of the language used.</p>_**", unsafe_allow_html=True)
    st.write(":red[_Dataset_:]  _https://ieee-dataport.org/documents/spam-sms-dravidian-languages#:~:text=Abstract,other%20contacts%20a%20Google%20form_")
    st.header("_Feature Extraction_", divider="red")
    data = {
        "Message": [
            "Dear Customer, +916300623587 is now available to take calls.",
            "Dear Customer, You have a missed call from +916300623587 The last missed call was at 06:26 PM on 29-Jan-2018 Thankyou, Team Jio.",
            "Join Hike to get Rs 40. Earn upto Rs. 10,000 by inviting your friends - http://go-hike.in/a/GqYeA1m1",
        ],
        "Label": [
            "ham", "ham", "spam"
        ]
    }
    df = pd.DataFrame(data)
    st.markdown(
        f"**_<p style='font-size:17px;'>The feature extraction process involved analyzing various aspects such as presence of :red[HTTP links, phone numbers, keywords, message length, emojis, special characters, and more], to comprehensively classify messages as spam or legitimate. A research paper titled :red[\"Evaluation of Hand-Crafted Features for the Classification of Spam SMS in Dravidian Languages\"] was published on Springer, elucidating the effectiveness of manually engineered features in discerning spam messages within Dravidian linguistic contexts.</p>_**", unsafe_allow_html=True)
    st.write(
        "_:red[Paper Link:] https://link.springer.com/chapter/10.1007/978-981-99-6755-1_1_")
    st.subheader("_Raw Dataset:_")
    st.dataframe(df)
    data = {
        "Label": [0, 0, 1],
        "has_http_link": [1, 1, 0],
        "has_phone_number": [0, 0, 0],
        "keywords": [60, 128, 100],
        "message_length": [0, 0, 0],
        "has_emoji": [1, 1, 1],
        "has_special_characters": [0, 0, 0],
        "has_money_symbols": [1, 0, 0],
        "has_emotion": [0, 0, 0],
        "has_greeting_words": [1, 1, 1],
        "has_self_answering_messages": [1, 1, 1],
        "has_random_capitalization": [1, 1, 1],
        "distinct_words": [8, 18, 12],
        "no_money_symbols": [0, 0, 0],
        "first_word": [0, 0, 0]
    }
    st.subheader("_Feature Extracted Dataset:_")
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.header("_Model Evaluation_", divider="red")
    st.markdown(
        f"**_<p style='font-size:17px;'>The upcoming evaluation presents crucial metrics, leveraging technical insights to assess the model's performance comprehensively.</p>_**", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col1.metric(":red[Accuracy]", 0.920131)
    col2.metric(":red[Precision]", 0.92001)
    col3.metric(":red[Recall]", 0.920131)
    col4.metric(":red[F1-Score]", 0.920069)
