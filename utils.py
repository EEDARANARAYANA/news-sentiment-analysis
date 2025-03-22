#Utility Functions

"""
Scraper:Fetches the top 10 news articles
Sentiment Analysis: Useful for finding the sentiment of the news
Topic Extraction: Useful for extracting the key topics or key words
Text-to-Speech Convertion in Hindi
"""

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS
import os
from deep_translator import GoogleTranslator

#For scrabing the news from the web browser, I used bbc api to extract the news articles
def scrape_news(company_name):
    search_url=f"https://www.bbc.co.uk/search?q={company_name}&filter=news"
    headers ={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    for item in soup.select("li a[href*='/news/']")[:10]:
        title = item.get_text(strip=True)
        link = item['href']
        if not link.startswith("https"):
            link = "https://www.bbc.co.uk"+link
        summary = extract_summary(link)

        articles.append({
            "Title":title,
            "Summary": summary,
        })
    return articles

#Extract a short summary from the news articles
def extract_summary(url):
    headers ={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")[:3]
    summary = " ".join([p.get_text(strip=True) for p in paragraphs])
    return summary

#Extracts the key topics from the news
def extract_topics(text):
    words = text.split()
    keywords = [word for word in words if word.istitle() and len(word)>3]
    return list(set(keywords[:5]))

#Function to perform sentiment analysis
def perform_sentiment_analysis(text):
    if not isinstance(text, str) or not text.strip():
        return "Neutral"
    polarity=TextBlob(text).sentiment.polarity
    if polarity>0:
        return "Positive"
    elif polarity<0:
        return "Negative"
    return "Neutral"
    
#Processing multiple articles for sentiment analysis
def perform_sentiment_analysis_for_articles(articles):
    results = []
    for article in articles:
        if isinstance(article, dict) and "Summary" in article:
            summary = article["Summary"]
            if isinstance(summary, list):
                summary = " ".join(str(s) for s in summary)
            sentiment = perform_sentiment_analysis(summary)
            article["Sentiment"]=sentiment
            results.append(article)
    return results

#Convertion of summary text into hindi speech
def convert_to_hindi_tts(articles):
    hindi_summaries = []
    
    for a in articles:
        if "Summary" in a and a["Summary"]:  
            translated_text = GoogleTranslator(source="en", target="hi").translate(a["Summary"])
            if translated_text and translated_text.strip():
                hindi_summaries.append(translated_text)
            else:
                print(f"Translation failed for: {a['Summary']}")  # Debugging

    hindi_text = " ".join(hindi_summaries)

    if not hindi_text.strip():  
        raise ValueError("No valid Hindi text available for TTS conversion.")

    tts = gTTS(text=hindi_text, lang="hi")
    audio_path = "hindi_summary.mp3"
    tts.save(audio_path)

    return audio_path


