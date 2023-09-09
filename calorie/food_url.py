from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
import csv

#foodがまとまっているページのURL
urls = ['https://product.starbucks.co.jp/food/?nid=mm',#季節のおすすめ
		'https://product.starbucks.co.jp/food/dessert/?purchase_methods=STARBUCKS_COFFEE&brand_code=starbucks-coffee',#デザート
		'https://product.starbucks.co.jp/food/pastry/?purchase_methods=STARBUCKS_COFFEE&brand_code=starbucks-coffee',#ぺすとりー
		'https://product.starbucks.co.jp/food/sandwich/?purchase_methods=STARBUCKS_COFFEE&brand_code=starbucks-coffee',#サンドイッチ
		'https://product.starbucks.co.jp/food/package/?purchase_methods=STARBUCKS_COFFEE&brand_code=starbucks-coffee',#パッケージフード
		'https://product.starbucks.co.jp/food/food-others/?brand_code=starbucks-coffee&purchase_methods=STARBUCKS_COFFEE']#その他

food_urls = []

それぞれのfoodのURLを取得
for url in urls:
	driver = webdriver.Chrome()
	driver.get(url)

	# class属性が"card__inner"の要素を取得
	elements = driver.find_elements(By.CLASS_NAME, 'card__inner')

	# 取得した要素からhref属性の値を取得
	for element in elements:
		href = element.get_attribute('href')
		if href:
			food_urls.append(href)

	# WebDriverをクローズ
	driver.quit()

datas = []

#foodのURLからカロリーと値段を取得
for url in food_urls:
	driver = webdriver.Chrome()

	driver.get(url)
	time.sleep(3)

	item_name = driver.find_element(By.CLASS_NAME, 'text-limit.text-bold')
	# 栄養成分情報を開く
	try:
		toggle_icon = driver.find_element(By.CLASS_NAME, 'alle-p-detail-toggle__head-icon')
		toggle_icon.click()
	except (NoSuchElementException, ElementNotInteractableException):
		continue
	except Exception as e:
		continue
	try:
		toggle_icon = driver.find_element(By.ID, 'click-tab-nutrient')
		toggle_icon.click()
	except (NoSuchElementException, ElementNotInteractableException):
		continue
	except Exception as e:
		continue

	nutrient_calory_tr = driver.find_element(By.ID, 'nutrient-calory')
	cal = nutrient_calory_tr.find_element(By.TAG_NAME, 'td')
	price = driver.find_element(By.CLASS_NAME, 'product-information__price')
	datas.append([item_name.text, cal.text.replace('kcal', ''), price.text.replace('￥', '')])
	
	driver.quit()

csv_file = "food.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
	writer = csv.writer(file)
	writer.writerow(["Menu Name", "Cal", "price"])  # ヘッダー行を書き込む
	i = 0
	for data in datas:
		writer.writerow([data[0], data[1], data[2]])
		i += 1
