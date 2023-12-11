import requests
from send_email import send_email

api_key = ""
url = "https://newsapi.org/v2/everything?q=python&from=2023-11-11&sortBy=publishedAt&apiKey="
request = requests.get(url)
content = request.json()
# print(content["articles"])

def get_message():
    message = ""
    for article in content["articles"]:        
        message += article["title"] + "\n" + article["url"] + "\n\n"
    return message

send_email(get_message().encode("utf-8"))
