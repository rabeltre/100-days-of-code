from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\driver_selenium\chromedriver.exe")

driver.get("https://www.google.com")
time.sleep(3)
displayelement = driver.find_element_by_name("btnI")
print(displayelement.is_enabled())
print(displayelement.is_displayed())

driver.close()