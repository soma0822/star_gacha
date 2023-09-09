import re
import requests
import csv
from bs4 import BeautifulSoup

# ターゲットのURL
url = "https://product.starbucks.co.jp/allergy/nutrient/"


datas = []

# GETリクエストを送信してHTMLを取得
response = requests.get(url)
html = response.text

# BeautifulSoupでHTMLを解析
soup = BeautifulSoup(html, "html.parser")

print(soup)

# メニュー名を抽出
# title_element = soup.find("title")
# if title_element:
# 	title_text = title_element.get_text()
# 	parts = title_text.split("|")
# 	menu_name = parts[0].strip()
# else:
# 	menu_name = "Title not found"

# # 正規表現を使用して価格情報を抽出
# price_pattern = r'"price_in_vat":(\d+),'
# prices = re.findall(price_pattern, html)

# # CSVファイルに書き込む
# sizes = ["Venti", "Grande", "Tall", "Short"]
# i = 0
# if len(prices) == 1:
# 	datas.append([menu_name, price])
# else:
# 	for price in prices:
# 		datas.append([menu_name + " " + sizes[i], price])
# 		i += 1
	
# # print(datas)
# csv_file = "menu_prices.csv"
# with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
# 	writer = csv.writer(file)
# 	writer.writerow(["Menu Name", "Price"])  # ヘッダー行を書き込む
# 	i = 0
# 	for data in datas:
# 		writer.writerow([data[0], data[1]])
# 		i += 1
# # for price in prices:
# # 	writer.writerow([menu_name + " " + sizes[i], price])
# # 	i += 1

# print("CSVファイルに保存しました:", csv_file)