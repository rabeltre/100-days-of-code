import scrapy

class TableSpider(scrapy.Spider):
    name = "table-scrapy"
    start_urls = ['https://getbootstrap.com/docs/4.5/content/tables/']
    
    def parse(self, response):
        for row in response.xpath('/html/body/div[2]/div/main/div[5]/table/tbody/tr'):
            yield {
                'first': row.xpath('td[1]//text()').extract_first(),
                'last': row.xpath('td[2]//text()').extract_first(),
                'handle': row.xpath('td[3]//text()').extract_first(),
            }