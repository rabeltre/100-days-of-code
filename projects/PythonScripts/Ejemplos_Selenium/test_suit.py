import unittest
from selenium import webdriver
import time
import HtmlTestRunner

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driver_selenium\chromedriver.exe")

    def tearDown(self) :
        self.driver.quit()

    def test_buscar(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elemento = driver.find_element_by_name("q")
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.ENTER)
        time.sleep(5)
        assert "No se encontro el elemento: " not in driver.page_source


    def test_usando_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        options = select.find_elements_by_tag_name("option")
        time.sleep(3)
        for option in options:
            print(f"Los valores son {option.get_attribute('value')}")
            option.click()
            time.sleep(1)

        seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(3)

    def test_usando_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(3)
        toggle = driver.find_element_by_xpath("//*[@id='main']/label[1]/div")
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Resultados de mi test plan'))