from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

options = Options()
#options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r"C:\driver_selenium\chromedriver.exe")

driver.get("https://outlook.live.com/owa/")

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "dynamicmarketredirect-dialog-close"))
    )
    driver.find_element_by_xpath('//*[@id="dynamicmarketredirect-dialog-close"]').click()
    driver.find_element_by_xpath('//*[@id="mectrl_main_trigger"]/div/div[1]').click()
except:
    driver.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a').click()

finally:
    driver.find_element_by_xpath('//*[@id="i0116"]').send_keys("email@outlook.com")
    driver.find_element(By.ID, "i0118").send_keys("password")
    driver.find_element(By.XPATH, "//*[@id='idSIButton9']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='idSIButton9']").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="id__3"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input').send_keys("rbeltrecastro@gmail.com")
    driver.find_element_by_xpath('//*[@id="sug-0"]/div/button[1]/span/div/div/div/div[2]/span[2]').click()
    driver.find_element_by_xpath('//*[@id="TextField126"]').send_keys("Test Selenium")
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]').send_keys("Esta es una prueba desde selenium")
    driver.find_element_by_xpath('//*[@id="id__130"]').click()

    time.sleep(5)
    driver.close()