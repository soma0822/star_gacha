import requests
from bs4 import BeautifulSoup

# ウェブページのURL
url = "https://product.starbucks.co.jp/beverage/drip/"

# ウェブページのHTMLを取得
response = requests.get(url)
html = response.content

# BeautifulSoupでHTMLを解析
soup = BeautifulSoup(html, "html.parser")

# メニュー名と値段を抽出して表示
menu_items = soup.find_all("li", class_="menu-item")
for item in menu_items:
    menu_name = item.find("h4").text.strip()
    price = item.find("p", class_="price").text.strip()
    print(f"メニュー名: {menu_name}")
    print(f"値段: {price}")
    print("=" * 30)