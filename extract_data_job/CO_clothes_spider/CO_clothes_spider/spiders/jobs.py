import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import re

class DieselItem(scrapy.Item):
    product_name = scrapy.Field()
    best_price = scrapy.Field()

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['co.diesel.com']
    start_urls = ['https://co.diesel.com/Hombre/Denim-y-Ropa/Ropa/Camisetas']
    

    def parse(self, response):
        for sel in response.xpath("//div[contains(@id, 'ResultItems_')]/div/ul/li/span"):
            item = DieselItem()
            item['product_name'] = sel.xpath("b[@class='product-name']/a/@title").extract()[0]
            item['best_price'] = re.search(r'\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})', sel.xpath("span[@class='price']/a/span[@class='best-price']/text()").extract()[0]).group(0)
            yield item