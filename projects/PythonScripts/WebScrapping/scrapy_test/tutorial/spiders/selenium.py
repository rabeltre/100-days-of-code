import scrapy
from scrapy_selenium import SeleniumRequest 

#https://github.com/clemfromspace/scrapy-selenium

class SeleniumSpider(scrapy.Spider):
    name = 'selenium'
    def start_requests(self): 
        yield SeleniumRequest( 
            url ="https://www.geeksforgeeks.org/", 
            wait_time = 3, 
            screenshot = True, 
            callback = self.parse,  
            dont_filter = True    
        ) 
        
        
    def parse(self, response):
        articulos = response.xpath('/html/body/div[2]/div/div/div[1]/div[2]/div') 
        next_page = response.css('a.nextpostslink::attr(href)').get()
        
        for articulo in articulos: 
            nombre_articulo = articulo.xpath('div/div[1]/a/text()').get()
            link_articulo = articulo.xpath('div/div[1]/a/@href').get()
            
            if nombre_articulo is not None:
                yield {
                    'nombre_articulo': nombre_articulo.split("\n")[0],
                    'link_articulo': link_articulo,
                    'next_page': next_page
                }
        
        if next_page is not None:
            yield SeleniumRequest( 
            url =next_page, 
            wait_time = 3, 
            screenshot = True, 
            callback = self.parse,  
            dont_filter = True    
        ) 
            
