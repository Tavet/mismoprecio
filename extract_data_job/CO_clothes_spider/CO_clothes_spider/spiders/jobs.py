import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile, logger
import re
import time

price_pattern = r'\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})'


class DieselItem(scrapy.Item):
    product_name = scrapy.Field()
    old_price = scrapy.Field()
    best_price = scrapy.Field()
    image_url = scrapy.Field()
    disc = scrapy.Field()

class JobsSpider(scrapy.Spider):
    logfile("openaq_spider.log", maxBytes=1e6, backupCount=3)
    name = 'jobs'
    allowed_domains = ['co.diesel.com']

    def start_requests(self):
        url = 'https://co.diesel.com/Hombre/Denim-y-Ropa/Ropa/Camisetas'
        yield scrapy.Request(url=url, callback=self.parse_tshirts)

    def scroll(self, driver, timeout):
        scroll_pause_time = timeout
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def parse_tshirts(self, response):
        driver = webdriver.Chrome('C:/Depayser/Best Deal Project/_static/drivers/chromedriver.exe')
        driver.get('https://co.diesel.com/Hombre/Denim-y-Ropa/Ropa/Camisetas')
        driver.implicitly_wait(30)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id, 'ResultItems_')]")))
        self.scroll(driver, 2)
        source = driver.page_source
        selector = Selector(text=source)
        logger.info(f"Selector: {selector}")
        
        for sel in selector.xpath("//div[contains(@id, 'ResultItems_')]/div/ul/li/span"):
            item = DieselItem()
            item['product_name'] = sel.xpath("b[@class='product-name']/a/@title").extract()[0]
            
            try:
                item['best_price'] = sel.xpath("span[@class='price']/a/span[@class='best-price']/text()").extract()[0]
            except IndexError:
                item['old_price'] = sel.xpath("span[@class='price']/a/span[@class='old-price']/text()").extract()[0]
                item['best_price'] = sel.xpath("span[@class='price']/a/span[@class='best-price widthC']/text()").extract()[0]
                item['disc'] = sel.xpath("span[@class='price']/span[@class='dtoF']/text()").extract()[0]


            item['image_url'] = sel.xpath("a[@class='product-image']/img/@src").extract()[0]
            yield item
