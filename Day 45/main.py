from bs4 import BeautifulSoup
import requests as req

response_url = req.get("https://news.ycombinator.com/")
url_text = response_url.text

soup = BeautifulSoup(url_text, "html.parser")
headlines = soup.select(selector=".titlelink")
headline = []
link = []
for news in headlines:
    headline.append(news.get_text())
    link.append(news.get("href"))
upvote = [int(score.get_text().split(" ")[0]) for score in soup.select(selector=".score")]

print(len(headline))
print(len(link))
print(len(upvote))




