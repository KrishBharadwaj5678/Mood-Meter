import streamlit as st
import requests

st.set_page_config(
    page_title="Mood Meter",
    page_icon="icon.png",
    menu_items={
        "About":"Mood Meter allows you to instantly understand the sentiment of any text, providing accurate and swift emotional insights."
    }
)

st.write("<h2 style='color:#FF4E88;font-size:37px;'>Accurate Sentiment Analysis in Seconds</h2>",unsafe_allow_html=True)

text=st.text_input("Your text here",placeholder="I'm loving it!")
btn=st.button("Analyze")
if btn:
    if(len(text)>=1):
        try:
            api_url = 'https://api.api-ninjas.com/v1/sentiment?text={}'.format(text)

            response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})

            if response.status_code == requests.codes.ok:
                data=response.json()
                sentiment=data['sentiment'].lower().split("_")
                modified_sentiment=" ".join(i.title() for i in sentiment)

                st.write(f"<h2 style='font-size:32px;color:#F4CE14;'>Text: {data['text']}</h2>",unsafe_allow_html=True)

                st.write(f"<h2 style='font-size:32px;color:#36C2CE;'>Sentiment: {modified_sentiment}</h2>",unsafe_allow_html=True)

                st.write(f"<h2 style='font-size:32px;color:#FF7F3E;'>Score: {data['score']}</h2>",unsafe_allow_html=True)
        except:
            st.error("Network Error 🔌")
    else:
        st.warning("Provide Some Text")
