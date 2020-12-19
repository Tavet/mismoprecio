# Scrapy
import scrapy
from scrapy.selector import Selector

# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile, logger

# Otros
import re
import time

price_pattern = r'\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})'


class DieselItem(scrapy.Item):
    product_name = scrapy.Field()  # Nombre del producto
    image_url = scrapy.Field()  # Imagen URL
    best_price = scrapy.Field()  # Precio
    old_price = scrapy.Field()  # Precio anterior (si tiene descuento)
    disc = scrapy.Field()  # Descuento
    url = scrapy.Field()  # URL del producto
    color_sku = scrapy.Field()  # Colores y tallas por color


class DieselSpider(scrapy.Spider):
    logfile("openaq_spider.log", maxBytes=1e6, backupCount=3)
    name = 'diesel'
    allowed_domains = ['co.diesel.com']

    def start_requests(self):
        url = 'https://co.diesel.com/Hombre/Denim-y-Ropa/Ropa'
        yield scrapy.Request(url=url, callback=self.parse_clothes)

    # Scroll function
    def scroll(self, driver, timeout):
        scroll_pause_time = timeout
        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def parse_clothes(self, response):
        driver = webdriver.Chrome(
            'C:/Depayser/Best Deal Project/_static/drivers/chromedriver.exe')
        driver.get('https://co.diesel.com/Hombre/Denim-y-Ropa/Ropa')
        driver.implicitly_wait(30)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@id, 'ResultItems_')]")))
        self.scroll(driver, 2)
        rootSelector = Selector(text=driver.page_source)
        logger.info(f"Root Selector: {rootSelector}")

        for sel in rootSelector.xpath("//div[contains(@id, 'ResultItems_')]/div/ul/li/span"):
            logger.info(f"Seleccionando un nuevo item para Diesel")
            item = DieselItem()
            item['product_name'] = sel.xpath(
                "b[@class='product-name']/a/@title").extract()[0]

            try:
                item['best_price'] = sel.xpath(
                    "span[@class='price']/a/span[@class='best-price']/text()").extract()[0]
            except IndexError:
                item['old_price'] = sel.xpath(
                    "span[@class='price']/a/span[@class='old-price']/text()").extract()[0]
                item['best_price'] = sel.xpath(
                    "span[@class='price']/a/span[@class='best-price widthC']/text()").extract()[0]
                item['disc'] = sel.xpath(
                    "span[@class='price']/span[@class='dtoF']/text()").extract()[0]

            item['image_url'] = sel.xpath(
                "a[@class='product-image']/img/@src").extract()[0]
            item['url'] = sel.xpath("a/@href").extract()[0]

            # Abrir cada item para obtener el color y el SKU (tallas)
            driver.find_element_by_tag_name(
                'body').send_keys(Keys.COMMAND + 't')
            driver.get(item['url'])

            # Esperar que cargue el color y las tallas
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//span[@class='group_0' and @class='group_1'] ")))

            # Encontrar los colores que no sean unavailable
            colors = driver.find_elements(
                By.XPATH, "//span[@class='group_0']/input[not(contains(@class,'item_unavaliable'))]")

            item['color_sku'] = []
            for color_item in colors:
                driver.execute_script("arguments[0].click();", color_item)
                time.sleep(2)
                itemSelector = Selector(text=driver.page_source)
                # Encontrar los tamaños para el color seleccionado
                sizes = itemSelector.xpath(
                    "//span[@class='group_1']/input[not(contains(@class,'item_unavaliable')) and not(contains(@class, 'item_doesnt_exist')) and not(contains(@class, 'combination_unavaliable'))]/@data-value").extract()
                if(sizes):
                    item['color_sku'].append({
                        "color": color_item.get_attribute("value"),
                        "sizes": sizes
                    })

            logger.info("OK")
            driver.find_element_by_tag_name(
                'body').send_keys(Keys.COMMAND + 'w')

            yield item