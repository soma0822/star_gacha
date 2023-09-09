from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

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
"https://menu.starbucks.co.jp/4524785526457",
"https://menu.starbucks.co.jp/4524785494176",
"https://menu.starbucks.co.jp/4524785461062",
"https://menu.starbucks.co.jp/4524785344143",
"https://menu.starbucks.co.jp/4524785165731",
"https://menu.starbucks.co.jp/4524785166059",
"https://menu.starbucks.co.jp/4524785165816",
"https://menu.starbucks.co.jp/4524785165892",
"https://menu.starbucks.co.jp/4524785165939",
"https://menu.starbucks.co.jp/4524785118751",
"https://menu.starbucks.co.jp/4524785526310",
"https://menu.starbucks.co.jp/4524785478985",
"https://menu.starbucks.co.jp/4524785537170",
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

def click_element_safely(driver, xpath):
	try:
		toggle_icon = driver.find_element(By.XPATH, xpath)
		toggle_icon.click()
	except (NoSuchElementException, ElementNotInteractableException):
		return None
	except Exception as e:
		return None

def get_calorie(driver, xpath):
	if click_element_safely(driver, 'alle-c-form-select') is None:
		return None
	if click_element_safely(driver, xpath) is None:
		return None

	nutrient_calory_tr = driver.find_element(By.ID, 'nutrient-calory')
	td_element = nutrient_calory_tr.find_element(By.TAG_NAME, 'td')
	return td_element.text.replace('kcal', '')

for url in urls:
	driver = webdriver.Chrome()

	driver.get(url)

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

	# サイズ選択があるかどうか
	time.sleep(1)
	toggle_icon = driver.find_element(By.ID, 'select-size')
	if toggle_icon == None:
		size = "Tall"
		nutrient_calory_tr = driver.find_element(By.ID, 'nutrient-calory')
		cal = nutrient_calory_tr.find_element(By.TAG_NAME, 'td')
		datas.append([item_name.text, size, cal.text])
	else:
		cal = get_calorie(driver, '//option[@data-value="1"]')
		if cal == None:
			driver.quit()
			continue
		datas.append([item_name.text, "Short", cal])
		cal = get_calorie(driver, '//option[@data-value="2"]')
		if cal == None:
			driver.quit()
			continue
		datas.append([item_name.text, "Short", cal])
		cal = get_calorie(driver, '//option[@data-value="3"]')
		if cal == None:
			driver.quit()
			continue
		datas.append([item_name.text, "Short", cal])
		cal = get_calorie(driver, '//option[@data-value="4"]')
		if cal == None:
			driver.quit()
			continue
		datas.append([item_name.text, "Short", cal])
	print(item_name.text)
	sys.stdout.flush()
	driver.quit()

csv_file = "menu_prices.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
	writer = csv.writer(file)
	writer.writerow(["Menu Name", "Size", "Price"])  # ヘッダー行を書き込む
	i = 0
	for data in datas:
		writer.writerow([data[0], data[1], data[2]])


