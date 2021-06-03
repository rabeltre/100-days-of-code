import requests
import xml.etree.ElementTree as ET
import re

url = "https://micm.gob.do/rss/combustibles.aspx"

response = requests.request("GET", url)

root = ET.fromstring(response.content)

item = {}
for child in root[0].find('item').iter():
    item[child.tag] = child.text

for i in item['description'].split('\n'):
    if "div" in i:
        # other_root = ET.fromstring()
        nombre_combustible = re.compile('<strong>(.*?)</strong').search(i)
        precio_combustible = re.compile('</strong>(.*?)</div').search(i)

        print(nombre_combustible.group(1), precio_combustible.group(1).replace('RD$', ''))





