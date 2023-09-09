import re
import requests
import csv
import time
from bs4 import BeautifulSoup

url = "https://product.starbucks.co.jp/food/?nid=mm"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')


print(soup)

# すべての<a>要素を取得
href_values = soup.find_all('a', class_='card__inner')

# 結果を表示
for href in href_values:
    print(href)