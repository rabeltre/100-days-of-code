from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\driver_selenium\chromedriver.exe")

driver.get("https://www.gmail.com/")

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("rbeltrecastro@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(2)

clave = driver.find_element_by_name("password")
clave.send_keys("tupasswordpersonal")
clave.send_keys(Keys.ENTER)