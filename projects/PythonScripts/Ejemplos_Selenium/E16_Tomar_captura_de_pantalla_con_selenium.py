from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(5)

driver.get_screenshot_as_file("C:\\Users\\rabel\maquinas_vagrants\\test\\100-days-of-code\\projects\\PythonScripts\\Ejemplos_Selenium\\image_test.png")

driver.close()