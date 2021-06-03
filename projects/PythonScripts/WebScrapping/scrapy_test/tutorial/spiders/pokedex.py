import scrapy
from datetime import datetime
from ..items import PokemonItem

class RatesSpider(scrapy.Spider):
    name = "pokedex"
    start_urls = ['https://pokemondb.net/pokedex/all']

    def parse(self, response):
        for row in response.xpath('//*[@id="pokedex"]/tbody/tr'):
            url_pokemon = 'https://pokemondb.net' + str(row.xpath('td[2]/a/@href').get())
            image_urls = row.xpath('td//@data-src').get()
            
            pokemon_information= {
                'number': row.xpath('td[1]/@data-sort-value').get(),
                'image_urls': str(image_urls),
                'images': image_urls.split("/")[-1],
                'name': row.xpath('td[2]/a/text()').get(),
                'url_pokemon': url_pokemon,
                'type': row.xpath('td[3]/a/text()').getall(),
                'total': row.xpath('td[4]/text()').get(),
                'HP': row.xpath('td[5]/text()').get(),
                'Attack': row.xpath('td[6]/text()').get(),
                'Defense': row.xpath('td[7]/text()').get(),
                'Sp_atk': row.xpath('td[8]/text()').get(),
                'Sp_Def': row.xpath('td[9]/text()').get(),
                'Speed': row.xpath('td[10]/text()').get()
            }
            
            request = scrapy.Request(url_pokemon,
                                callback=self.pokemon_details)
            
            request.cb_kwargs['pokemon_information'] = pokemon_information
            
            yield request
    
    def pokemon_details(self, response, pokemon_information):
        weight_path='//*[@id="tab-basic-{number}"]/div[1]/div[2]/table/tbody/tr[5]/td/text()'.format(number=pokemon_information['number'])
        weight_info = response.xpath(weight_path).get()
        pokemon_information['Weight'] = weight_info.replace(u'\u00a0', u' ')
        
        pokemon = PokemonItem(pokemon_information)
        yield pokemon
        
            
    """        
    def parse(self, response):
        request = scrapy.Request('http://www.example.com/index.html',
                                callback=self.parse_page2,
                                cb_kwargs=dict(main_url=response.url))
        request.cb_kwargs['foo'] = 'bar'  # add more arguments for the callback
        yield request

    def parse_page2(self, response, main_url, foo):
        yield dict(
            main_url=main_url,
            other_url=response.url,
            foo=foo,
        )
"""