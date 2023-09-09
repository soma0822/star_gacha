import requests
from bs4 import BeautifulSoup

# URLを指定
url = "https://product.starbucks.co.jp/beverage/beverage-others/"

# GETリクエストを送信してHTMLを取得
response = requests.get(url)

html = response.content

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")

# 各リンクのhref属性からURLを取得
for link in links:
    href = link.get("href")
    if href:
        print("Link URL:", href)