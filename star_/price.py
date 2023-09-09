import re
import requests
import csv
import time
from bs4 import BeautifulSoup

# ターゲットのURL
urls = [
"https://menu.starbucks.co.jp/4524785000018",
"https://menu.starbucks.co.jp/4524785062870",
"https://menu.starbucks.co.jp/4524785324732",
"https://menu.starbucks.co.jp/4524785046856",
"https://menu.starbucks.co.jp/4524785000223",
"https://menu.starbucks.co.jp/4524785047396",
"https://menu.starbucks.co.jp/4524785433106",
"https://menu.starbucks.co.jp/4524785433021",
"https://menu.starbucks.co.jp/4524785000285",
"https://menu.starbucks.co.jp/4524785000254",
"https://menu.starbucks.co.jp/4524785034532",
"https://menu.starbucks.co.jp/4524785019232",
"https://menu.starbucks.co.jp/4524785000315",
"https://menu.starbucks.co.jp/4524785000346",
"https://menu.starbucks.co.jp/4524785344075",
"https://menu.starbucks.co.jp/4524785487253",
"https://menu.starbucks.co.jp/4524785457690",
"https://menu.starbucks.co.jp/4524785344143",
"https://menu.starbucks.co.jp/4524785165731",
"https://menu.starbucks.co.jp/4524785166059",
"https://menu.starbucks.co.jp/4524785165816",
"https://menu.starbucks.co.jp/4524785165892",
"https://menu.starbucks.co.jp/4524785165939",
"https://menu.starbucks.co.jp/4524785118751",
"https://menu.starbucks.co.jp/4524785526310",
"https://menu.starbucks.co.jp/4524785461154",
"https://menu.starbucks.co.jp/4524785034204",
"https://menu.starbucks.co.jp/4524785154681",
"https://menu.starbucks.co.jp/4524785106499",
"https://menu.starbucks.co.jp/4524785304970",
"https://menu.starbucks.co.jp/4524785305465",
"https://menu.starbucks.co.jp/4524785305076",
"https://menu.starbucks.co.jp/4524785492820",
"https://menu.starbucks.co.jp/4524785024748",
"https://menu.starbucks.co.jp/4524785349193",
"https://menu.starbucks.co.jp/4524785305328",
"https://menu.starbucks.co.jp/4524785305366",
"https://menu.starbucks.co.jp/4524785305571",
"https://menu.starbucks.co.jp/4524785309104",
"https://menu.starbucks.co.jp/4524785155473",
"https://menu.starbucks.co.jp/4524785492868",
"https://menu.starbucks.co.jp/4524785000674",
"https://menu.starbucks.co.jp/4524785046900",
"https://menu.starbucks.co.jp/4524785000735",
"https://menu.starbucks.co.jp/4524785000858",
"https://menu.starbucks.co.jp/4524785000865",
"https://menu.starbucks.co.jp/4524785216341",
"https://menu.starbucks.co.jp/4524785216334",
"https://menu.starbucks.co.jp/4524785374188",
"https://menu.starbucks.co.jp/4524785374171"
]

datas = []

# GETリクエストを送信してHTMLを取得
for url in urls:

	response = requests.get(url)
	html = response.text

	# BeautifulSoupでHTMLを解析
	soup = BeautifulSoup(html, "html.parser")

	# メニュー名を抽出
	title_element = soup.find("title")
	if title_element:
		title_text = title_element.get_text()
		parts = title_text.split("|")
		menu_name = parts[0].strip()
	else:
		menu_name = "Title not found"

	# 正規表現を使用して価格情報を抽出
	price_pattern = r'"price_in_vat":(\d+),'
	prices = re.findall(price_pattern, html)

	# CSVファイルに書き込む
	sizes = ["Venti", "Grande", "Tall", "Short"]
	i = 0
	if len(prices) == 1:
		datas.append([menu_name, price])
	else:
		for price in prices:
			datas.append([menu_name + " " + sizes[i], price])
			i += 1
	
# print(datas)
csv_file = "menu_prices.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
	writer = csv.writer(file)
	writer.writerow(["Menu Name", "Price"])  # ヘッダー行を書き込む
	i = 0
	for data in datas:
		writer.writerow([data[0], data[1]])
		i += 1
# for price in prices:
# 	writer.writerow([menu_name + " " + sizes[i], price])
# 	i += 1

print("CSVファイルに保存しました:", csv_file)