import requests

api_key = "751aa5c95c6d4ffab434a38f93f35163"
url = "https://newsapi.org/v2/everything?q=python&from=2023-11-11&sortBy=publishedAt&apiKey=751aa5c95c6d4ffab434a38f93f35163"
request = requests.get(url)
content = request.json()
# print(content["articles"])

for article in content["articles"]:
    print(article["title"])
    print(article["url"])
   