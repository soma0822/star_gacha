# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
# import time
# import csv
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# url = 'https://dyf.starbucks.co.jp/menu/'

# data = []

# driver = webdriver.Chrome()
# driver.get(url)

# wait = WebDriverWait(driver, 10)

# index = 0
# while True:
# 	try:
# 		li_elements = driver.find_elements(By.CLASS_NAME, 'active02')
# 		if index >= len(li_elements):
# 			break

# 		element = li_elements[index]
# 		print(element.text)
# 		time.sleep(3)
# 		element.click()
# 		# hot_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hot')))
# 		# hot_icon.click()
# 		time.sleep(1)
# 		choice_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'choice02')))
# 		choice_icon.click()
# 		time.sleep(3)

# 		i = 0
# 		while True:
# 			try:
# 				portraitElements = driver.find_elements(By.CSS_SELECTOR, ".containerInner.landscape li")
# 				if i >= len(portraitElements):
# 					break
# 				prtraitElement = portraitElements[i]
# 				print(prtraitElement.text)
# 				prtraitElement.click()
# 				cos_element = driver.find_element_by_xpath('//a[@onclick="toDetail()"]')
# 				cos_element.click()
# 				time.sleep(3)
# 				element = driver.find_element_by_xpath('//span[@data-customize="howToOrder"]')
# 				print(element.text)
# 				driver.back()
# 				driver.refresh()
# 				i += 1
				
# 			except Exception as e:
# 				print(e)
# 				break



# 		driver.back()
# 		driver.refresh()
# 		index += 1
# 	except Exception as e:
# 		print(e, index)
# 		break

# # driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://dyf.starbucks.co.jp/menu/'

driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)

index = 6
while True:
	try:
		li_elements = driver.find_elements(By.CLASS_NAME, 'active01')
		if index >= len(li_elements):
			break

		element = li_elements[index]
		print(element.text)
		time.sleep(3)
		element.click()
		hot_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hot')))
		hot_icon.click()
		time.sleep(1)
		choice_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'choice02')))
		choice_icon.click()
		time.sleep(3)

		i = 0
		while True:
			try:
				portraitElements = driver.find_elements(By.CSS_SELECTOR, ".containerInner.landscape li")
				if i >= len(portraitElements):  # ここを修正
					break
				portraitElement = portraitElements[i]  # 変数名を修正
				print(portraitElement.text)
				portraitElement.click()  # 正しい要素をクリック
				cos_element = driver.find_element(By.XPATH, '//a[@onclick="toDetail()"]')
				cos_element.click()
				time.sleep(3)
				element = driver.find_element(By.XPATH, '//span[@data-customize="howToOrder"]')
				print(element.text)
				driver.back()
				driver.refresh()
				i += 1
				
			except Exception as e:
				print(e)
				break

		driver.back()
		driver.refresh()
		index += 1
		print('---------------------------')
	except Exception as e:
		print(e, index)
		break

driver.quit()
