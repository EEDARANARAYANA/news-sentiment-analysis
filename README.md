# News Summarization and Sentiment Analysis with Hindi TTS

## Project Overview
This project is a web-based application that extracts key details from news articles related to a given company. It performs sentiment analysis, comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool allows users to input a company name and receive a structured sentiment report along with an audio output. The application is deployed on Hugging Face Spaces and is built using **Streamlit** and **FastAPI**.

---

## Features
1. **News Extraction:** Fetches news articles using BeautifulSoup from BBC News.
2. **Sentiment Analysis:** Analyzes the sentiment of news summaries (Positive, Negative, Neutral).
3. **Comparative Analysis:** Highlights sentiment differences across articles.
4. **Text-to-Speech (TTS):** Converts the sentiment report to Hindi speech using gTTS.
5. **User Interface:** A web-based interface using Streamlit.
6. **API Backend:** Built using FastAPI to handle data processing and API communication.

---

## Installation
### Prerequisites
- Python 3.8+
- Pip

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd news-sentiment-analysis
   ```
2. Install required packages:
   ```bash
   pip install -r Requirements.txt
   ```

---

## Running the Application
### Backend (FastAPI)
Start the FastAPI server:
```bash
python -m uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend (Streamlit)
Start the Streamlit frontend:
```bash
python -m streamlit run app.py
```

---

## Usage
1. Open the Streamlit app in your browser.
2. Enter the company name and click 'Analyze News'.
3. View the sentiment analysis results, including topics and sentiment scores.
4. Listen to the Hindi TTS audio summarization.

---

## Deployment
The application is deployed on Hugging Face Spaces. Visit the link to access it:  
[Deployment Link](<huggingface-link>)

---

## Troubleshooting
- If the audio does not play, ensure the file path is correct and that the TTS conversion succeeded.
- In case of connectivity issues, make sure the FastAPI server is running.

---

## Acknowledgements
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [gTTS](https://pypi.org/project/gTTS/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)

