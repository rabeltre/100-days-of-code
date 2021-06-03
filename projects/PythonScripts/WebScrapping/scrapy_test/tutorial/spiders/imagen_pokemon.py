import scrapy
from datetime import datetime
from ..items import PokemonImagen

class RatesSpider(scrapy.Spider):
    name = "imagen"
    start_urls = ['https://pokemondb.net/pokedex/all']

    def parse(self, response):
        for row in response.xpath('//*[@id="pokedex"]/tbody/tr'):
            pokemonImagen = PokemonImagen()
            image_urls = row.xpath('td//@data-src').get()
            
            pokemonImagen['image_urls']= str(image_urls),
            pokemonImagen['images'] = image_urls.split("/")[-1]            

            yield pokemonImagen