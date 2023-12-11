import requests
from send_email import send_email
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv("SECRET_KEY")


def get_message():
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = secret_key
    KEY_WORD = "python, -swallows, -swallowed"
    LANGUAGE = "en"
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": KEY_WORD,
        "language": LANGUAGE,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    twenty_articles = articles[:20]
    subject = "Subject: Top 20 news about Python\n"
    message = "{}".format(subject)
    for article in twenty_articles:
        message += article["title"] + "\n" + article["url"] + "\n\n"
    return message



send_email(get_message().encode("utf-8"))
