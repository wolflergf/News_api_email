# Import necessary modules
import requests
from send_email import send_email
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the secret key from environment variables
secret_key = os.getenv("SECRET_KEY")


# Function to fetch and format the news articles
def get_message():
    # Define the endpoint and parameters for the NewsAPI
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = secret_key
    KEY_WORD = "python, -swallows, -swallowed"
    LANGUAGE = "en"
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": KEY_WORD,
        "language": LANGUAGE,
    }

    # Make a GET request to the NewsAPI
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)

    # Extract the articles from the response
    articles = news_response.json()["articles"]

    # Get the top 20 articles
    twenty_articles = articles[:20]

    # Format the email subject
    subject = "Subject: Top 20 news about Python\n"

    # Start the email message with the subject
    message = "{}".format(subject)

    # Add each article title and URL to the email message
    for article in twenty_articles:
        message += article["title"] + "\n" + article["url"] + "\n\n"

    # Return the formatted email message
    return message


# Send the email with the news articles
send_email(get_message().encode("utf8"))
