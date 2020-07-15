
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"C:\driver_selenium\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(5)
"""
valor = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[1]/th[1]').text
print(valor)


valor = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[2]/td[1]').text
print(valor)

valor = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[2]/td[2]').text
print(valor)

valor = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[2]/td[3]').text
print(valor)
"""
row = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr'))

col = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th'))

for n in range(2, row+1):
    for b in range(1, col+1):
        dato= driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr['+ str(n)+']/td['+str(b)+']').text
        print(dato, end='')
    print()


driver.close()



