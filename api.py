#running the fastapi
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils import scrape_news, perform_sentiment_analysis_for_articles, extract_topics,convert_to_hindi_tts
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message":"News Sentiment Analysis API is running!"}

class CompanyRequest(BaseModel):
    company_name: str

@app.post("/analyze")
def analyze_news(request: CompanyRequest):
    company_name=request.company_name

    articles = scrape_news(company_name)
    articles = perform_sentiment_analysis_for_articles(articles)
    for article in articles:
        article["Topics"]= extract_topics(article["Summary"])

    hindi_audio_file = convert_to_hindi_tts(articles)

    #Prepare JSON Response
    response = {
        "Company": company_name,
        "Articles": [
            {
                "Title": article["Title"],
                "Summary": article["Summary"],
                "Sentiment": article["Sentiment"],
                "Topics": article["Topics"]
            }
            for article in articles
        ],
        "Hindi_TTS_Audio": hindi_audio_file
    }

    return JSONResponse(content=response, status_code=200)

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#running the fastapi
#python -m uvicorn api:app --host 0.0.0.0 --port 8000 --reload

