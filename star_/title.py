import requests
from bs4 import BeautifulSoup

# URLを指定
url = "https://menu.starbucks.co.jp/4524785000018"

# GETリクエストを送信してHTMLを取得
response = requests.get(url)

html = response.content

# BeautifulSoupでHTMLを解析
soup = BeautifulSoup(html, "html.parser")

# メニュー名と値段を抽出して表示
title_element = soup.find("title")
if title_element:
    title_text = title_element.get_text()
    print("Title:", title_text)
else:
    print("Title not found")
	
title_element = soup.find("title")
if title_element:
    title_text = title_element.get_text()
    print("Title:", title_text)
else:
    print("Title not found")