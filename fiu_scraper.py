from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
web = 'https://www.audible.com/search'
path = 'C:\\Users\\moreiimo\\Documents\\Coding\\Repos\\FIU-Scraper\\driver\\chromedriver\\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(web)
product = driver.find_elements(by='xpath', value = '//li[contains(@class, "productListItem")]')


time.sleep(500)