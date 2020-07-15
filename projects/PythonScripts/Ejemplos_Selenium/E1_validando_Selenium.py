from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\driver_selenium\chromedriver.exe")

driver.get("http://python.org")
