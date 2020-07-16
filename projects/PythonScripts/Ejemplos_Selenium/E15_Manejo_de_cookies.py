from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(5)

all_cookies = driver.get_cookies()


for item in all_cookies:
    print(item)
driver.close()