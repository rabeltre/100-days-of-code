import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    unittest.main()

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driver_selenium\chromedriver.exe")

    def test_usando_implict_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("http://www.google.com")
        myDinamicElement = driver.find_element_by_name("q")

