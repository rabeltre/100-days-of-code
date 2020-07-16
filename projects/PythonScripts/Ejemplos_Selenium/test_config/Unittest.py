import unittest
import configparser
from selenium import webdriver

class usando_unittest(unittest.TestCase):

    def setUp(self):
        configuracion = configparser.ConfigParser()
        configuracion.read('config.cfg')
        configuracion.sections()
        gexplorer = configuracion['General']['chrome']
        self.page = configuracion['Paginas']['google']
        self.driver = webdriver.Chrome(executable_path=gexplorer)

    def test_usando_implit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(self.page)
        #myDynamicElement = driver.find_element_by_name("q")
        myDynamicElement = driver.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a')
        print(myDynamicElement.text)
        driver.implicitly_wait(5)
if __name__ == '__main__':
    unittest.main()