from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\driver_selenium\chromedriver.exe")

driver.get("https://www.w3schools.com/")
time.sleep(3)
encontrar_link = driver.find_element_by_link_text("Learn jQuery")

encontrar_link.click()

time.sleep(5)

driver.close()