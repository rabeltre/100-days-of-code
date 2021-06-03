# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonItem(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()
    url_pokemon = scrapy.Field()
    type = scrapy.Field()            
    total = scrapy.Field()           
    HP = scrapy.Field()            
    Attack = scrapy.Field()        
    Defense = scrapy.Field()         
    Sp_atk = scrapy.Field()           
    Sp_Def = scrapy.Field()        
    Speed = scrapy.Field()         
    Weight = scrapy.Field()  
    
class PokemonImagen(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
        
class AutoInfo(scrapy.Item):
    name = scrapy.Field()
    precio = scrapy.Field()
    moneda = scrapy.Field()
    card_url = scrapy.Field()
    next_href = scrapy.Field()
    
class AutoDetails(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    fecha_posteo = scrapy.Field()
    precio = scrapy.Field()
    moneda = scrapy.Field()
    marca = scrapy.Field()
    modelo = scrapy.Field()
    tipo = scrapy.Field()
    year = scrapy.Field()
    kilometraje = scrapy.Field()
    combustible = scrapy.Field()
    transmision = scrapy.Field()
    traccion = scrapy.Field()
    motor = scrapy.Field()
    
    
    

