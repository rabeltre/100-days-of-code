from Banco import Entidad
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import entidad_conexion_db




def scrapping_dolar():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #driver = webdriver.Chrome(executable_path=r"C:\driver_selenium\chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options, executable_path=r"C:\driver_selenium\chromedriver.exe")

    driver.get("https://www.infodolar.com.do/")
    row = len(driver.find_elements_by_xpath('//*[@id="Dolar"]/tbody/tr'))
    lista_entidades = []
    for i in range(1, row+1):
        entidad = Entidad()
        entidad.id = i
        entidad.name = driver.find_element_by_xpath('//*[@id="Dolar"]/tbody/tr[' + str(i) +']/td[1]/span').text
        entidad.compra = (driver.find_element_by_xpath('//*[@id="Dolar"]/tbody/tr[' + str(i) +']/td[2]').text)[3:8]
        entidad.venta = (driver.find_element_by_xpath('//*[@id="Dolar"]/tbody/tr[' + str(i) + ']/td[3]').text)[3:8]
        if entidad.venta != '':
            entidad.variacion = driver.find_element_by_xpath('//*[@id="Dolar"]/tbody/tr[' + str(i) + ']/td[4]/span/span').text
        entidad.spread = driver.find_element_by_xpath('//*[@id="Dolar"]/tbody/tr[' + str(i) + ']/td[5]').text
        #entidad.ultima_actualizacion = driver.find_element_by_xpath('//*[@id="Dolar"]/tbody/tr[' + str(i) + ']/td[6]/abbr').text

        lista_entidades.append(entidad)
    driver.quit()
    return lista_entidades



def scrapping_euro():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, executable_path=r"C:\driver_selenium\chromedriver.exe")
    #driver = webdriver.Chrome(executable_path=r"C:\driver_selenium\chromedriver.exe")
    driver.get("https://www.infodolar.com.do/precio-euro.aspx")

    row = len(driver.find_elements_by_xpath('//*[@id="cotizaciones"]/tbody/tr'))
    lista_entidades = []
    for i in range(1, row+1):
        entidad = Entidad()
        entidad.id = i
        entidad.moneda = 'EUR'
        entidad.name = driver.find_element_by_xpath('//*[@id="cotizaciones"]/tbody/tr[' + str(i) +']/td[1]/span').text
        entidad.compra = (driver.find_element_by_xpath('//*[@id="cotizaciones"]/tbody/tr[' + str(i) +']/td[2]').text)[3:8]

        entidad.venta = (driver.find_element_by_xpath('//*[@id="cotizaciones"]/tbody/tr[' + str(i) + ']/td[3]').text)[3:8]

        if entidad.venta != '':
            entidad.variacion = driver.find_element_by_xpath('//*[@id="cotizaciones"]/tbody/tr[' + str(i) + ']/td[4]/span/span').text
        entidad.spread = driver.find_element_by_xpath('//*[@id="cotizaciones"]/tbody/tr[' + str(i) + ']/td[5]').text
        #entidad.ultima_actualizacion = driver.find_element_by_xpath('//*[@id="Dolar"]/tbody/tr[' + str(i) + ']/td[6]/abbr').text
        lista_entidades.append(entidad)
    driver.quit()

    return lista_entidades

for item in entidad_conexion_db.buscar_todas_las_entidades():
    print(item)

"""
euro_list = scrapping_euro()
print("Euro")
for item in euro_list:
    entidad_conexion_db.agregar_entidad(item)

"""
dolar_list = scrapping_dolar()
print("Dolar")
for item in dolar_list:
    entidad_conexion_db.agregar_entidad(item)







