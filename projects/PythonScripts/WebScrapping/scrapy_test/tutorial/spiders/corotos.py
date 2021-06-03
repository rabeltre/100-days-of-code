import scrapy
from ..items import AutoInfo
from ..items import AutoDetails


class CorotosSpider(scrapy.Spider):
    name = 'corotos'
    start_urls = ['https://www.corotos.com.do/c/veh%C3%ADculos?page=1']

    def parse(self, response):
        base_url = 'https://www.corotos.com.do'
        auto_post = response.xpath('//*[@id="items-container"]/div')
        next_href = response.xpath('//*[@id="load-more-listings"]/@href').get()
        
        
        for row in auto_post:
            href = row.xpath('div/div[1]/a/@href').get()
            if href is not None:
                request = scrapy.Request(str(base_url + href),
                                callback=self.auto_details)
                yield request
                
                
        if next_href is not None:
            next_page = base_url + next_href
            yield scrapy.Request(next_page, callback=self.parse)

            
    def auto_details(self, response):
        autoDetails = AutoDetails()
        #autoDetails['name'] = response.xpath('/html/body/main/div/div[2]/div[1]/div[2]/h1/text()').get()
        page_price = response.css('h2.post__price::text').get()
        autoDetails['url'] = response.url
        autoDetails['fecha_posteo'] = str(response.css('p.post__date::text').get())
        autoDetails['name'] = response.css('h1.post__title::text').get()
        autoDetails['moneda'] = page_price.split()[0]
        autoDetails['precio'] = page_price.split()[1] if autoDetails['moneda'] != 'Gratis' else 0
                
        autoDetails['marca'] = response.xpath('/html/body/main/div/div[2]/div[2]/ul/li[1]/span[2]/span/text()').get()
        autoDetails['modelo'] = response.xpath('/html/body/main/div/div[2]/div[2]/ul/li[2]/span[2]/span/text()').get()
        autoDetails['tipo'] = response.xpath('/html/body/main/div/div[2]/div[2]/ul/li[3]/span[2]/span/text()').get()
        autoDetails['year'] = response.xpath('/html/body/main/div/div[2]/div[2]/ul/li[4]/span[2]/span/text()').get()
        autoDetails['kilometraje'] = response.xpath('/html/body/main/div/div[2]/div[2]/ul/li[5]/span[2]/span/text()').get()
        autoDetails['combustible'] = response.xpath('/html/body/main/div/div[2]/div[2]/ul/li[6]/span[2]/span/text()').get()
        autoDetails['transmision'] = response.xpath('/html/body/main/div/div[2]/div[2]/ul/li[7]/span[2]/span/text()').get()
        autoDetails['traccion'] = response.xpath('/html/body/main/div/div[2]/div[2]/ul/li[8]/span[2]/span/text()').get()
        autoDetails['motor'] = response.xpath('/html/body/main/div/div[2]/div[2]/ul/li[12]/span[2]/span/text()').get()
        
        yield autoDetails
        
            
                
        
        """
       
        if next_href is not None:
            next_page = base_url + next_href
            yield scrapy.Request(next_page, callback=self.parse)
        """
        
            