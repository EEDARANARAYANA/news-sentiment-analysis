#Frontend UI with Streamlit
"""
Takes the input
Calls the FastAPI backend
Displays news articles, sentiments, and topics
Plays the Hindi TTS Audio.
"""

import streamlit as st
import requests

st.set_page_config(page_title="News Analysis", layout="wide")
st.title("News Summarization & Sentiment Analysis")
company_name = st.text_input("Enter the Company name:")

if st.button("Analyze News"):
    if not company_name.strip():
        st.warning("Please enter a valid company name")
        st.stop()
    
    with st.spinner("Fetching news...."):
        response = requests.post("http://127.0.0.1:8000/analyze", json={"company_name": company_name})
        response.raise_for_status()
        data=response.json()

    if "error" in data:
        st.error(f"{data['error']}")
        st.stop()
    
    st.subheader(f"News Analysis for {data['Company']}")

    for article in data["Articles"]:
        st.markdown(f"{article['Title']}")
        st.write(f"Summary: {article['Summary']}")
        st.write(f"Sentiment: {article['Sentiment']}")
        st.write(f"Topics: {', '.join(article['Topics'])}")
        st.markdown("---")
    
    audio_file = data.get("Hindi_TTS_Audio")
    if audio_file:
        st.audio(audio_file, format="audio/mp3")
    else:
        st.error("Failed to generate TTS audio")

#run the frontend
#python -m streamlit run app.py