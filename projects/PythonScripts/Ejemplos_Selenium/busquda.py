from  selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time

palabra_buscada = "sele"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"C:\driver_selenium\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(3)

busqueda = driver.find_element_by_name("q")
busqueda.send_keys(palabra_buscada)
time.sleep(3)

for i in range(1, 11):
    elemento = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/ul/li[' + str(i) + ']/div/div[2]/div/span').text
    print(elemento)

driver.close()