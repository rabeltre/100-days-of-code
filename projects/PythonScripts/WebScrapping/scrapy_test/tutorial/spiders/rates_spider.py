import scrapy
from datetime import datetime

import unicodedata


class RatesSpider(scrapy.Spider):
    name = "rates"
    start_urls = ['https://www.infodolar.com.do']
    
 
    def parse(self, response):
        for row in response.xpath('//*[@id="Dolar"]/tr'):
            buy = row.xpath('td[2]//text()').extract_first()
            sell = row.xpath('td[3]//text()').extract_first()
            name = row.xpath('td[1]/span//text()').extract_first()
            
            yield {
                'name': name,
                'buy': buy.replace(u'\r\n                                ', u'').replace(u'$', u''),
                'sell': sell.replace(u'\r\n                                ', u'').replace(u'$', u''),
      
                'update': datetime.now().strftime("%d-%m-%y %H:%M:%S"),
            }