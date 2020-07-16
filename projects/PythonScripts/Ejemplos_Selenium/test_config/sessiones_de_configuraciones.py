import configparser

configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome':'C:\driver_selenium\chromedriver.exe'}
configuracion['Paginas'] = {'google': 'https://www.google.com'}

with open('config.cfg', 'w') as archivoconfig:
    configuracion.write(archivoconfig)