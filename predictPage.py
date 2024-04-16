import streamlit as st
from request import req


def process_text(text, dictionary):
    result = []
    for word in text.split():
        found = False
        for key, value in dictionary.items():
            if word.lower() in key.lower().split():
                result.append((word, value))
                found = True
                break
        if not found:
            result.append(word)
    return result


def annotate_text(text, prediction, vectors):
    exchanged_dict = {value: key for key, values in vectors.items()
                      for value in values}
    filtered_dict = {key: value for key,
                     value in exchanged_dict.items() if len(str(key)) > 0 and key != "yo"}
    from annotated_text import annotated_text
    colx, coly = st.columns(2)
    if prediction == "Spam":
        colx.metric("_Prediction_", prediction)

    else:
        colx.metric("_Prediction_", prediction)

    with coly:
        coly.metric(f"Features:", "")
        annotated_text(*tuple(filtered_dict.items()))


def page():
    st.title("_Multilingual_ SMS :red[Spam] Prediction")
    st.markdown(
        f"**_<p style='font-size:13px;'>:red[GitHub Repo:] : https://github.com/SAKTHIPRAKASH28/Multilingual-SMS-Spam-Prediction-API </p>_**", unsafe_allow_html=True)

    st.header("_Enter your :red[message]:_    ")
    text_input = st.text_area("None", label_visibility='hidden')

    col1, col2, col3 = st.columns([1, 10, 1])

    with col2:
        if st.button("Submit", key='submit_button', type="primary"):
            reponse = req(text_input)
            annotate_text(
                text_input, reponse["prediction"], reponse["vectors"])
