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
from selenium.common.exceptions import TimeoutException
from logzero import logfile, logger

# Otros
import os
import io
import re
import time
import json
import boto3

price_pattern = r'\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})'


class DieselItem(scrapy.Item):
    product_name = scrapy.Field()  # Nombre del producto
    image_url = scrapy.Field()  # Imagen URL
    best_price = scrapy.Field()  # Precio
    old_price = scrapy.Field()  # Precio anterior (si tiene descuento)
    disc = scrapy.Field()  # Descuento
    url = scrapy.Field()  # URL del producto
    color_sku = scrapy.Field()  # Colores y tallas por color
    description = scrapy.Field()  # Descripción del producto
    reference = scrapy.Field()  # Referencia (business key)
    category = scrapy.Field() # Categoría como "Ropa" o "Accesorios"
    subcategory = scrapy.Field() # Subscategoría como "Pantalones" o "Ropa interior"


class DieselSpider(scrapy.Spider):
    logfile("openaq_spider.log", maxBytes=1e6, backupCount=3)
    name = 'diesel'
    allowed_domains = ['co.diesel.com']

    def start_requests(self):
        yield scrapy.Request(url='https://co.diesel.com', callback=self.parse_clothes)

    def get_clothes_data(self):
        BUCKET_NAME = "best-deal-stores-info"
        FILE_NAME = "clothes/clothes.json"
        s3 = boto3.resource('s3',
                       aws_access_key_id='AKIARSJCFIURQ42RWPFY',
                       aws_secret_access_key='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'
                     )
        data = s3.Object(BUCKET_NAME, FILE_NAME).get()['Body'].read().decode('utf-8')
        json_data = json.loads(data)
        return [x for x in json_data if x['store'] == 'diesel'][0]


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
        logger.info(f"Iniciando proceso de recolección para Diesel")
        logger.info("Yeah 2")
        data = self.get_clothes_data()
        for clothes in data['content']:
            for category in clothes['content']:
                # item['category'] = category
                
                print(category)
        logger.info("Yeah 3")
        driver = webdriver.Chrome(
            'C:/Depayser/Best Deal Project/_static/drivers/chromedriver.exe')
        driver.get('https://co.diesel.com/Hombre/Denim-y-Ropa/Ropa')
        driver.implicitly_wait(30)
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@id, 'ResultItems_')]")))
        self.scroll(driver, 3)
        rootSelector = Selector(text=driver.page_source)
        clothes = rootSelector.xpath(
            "//div[contains(@id, 'ResultItems_')]/div/ul/li/span")

        for sel in clothes:
            item = DieselItem()
            logger.info(f"Seleccionando un nuevo item para Diesel")
            # *** Product name
            # Skip si no tiene nombre
            try:
                item['product_name'] = sel.xpath(
                    "b[@class='product-name']/a/@title").extract()[0]
            except IndexError as error:
                logger.error(f"Error fetching name: {error}")
                continue

            logger.info(f"Producto {item['product_name']}")

            # *** Price
            # Skip si no tiene precio
            try:
                item['best_price'] = sel.xpath(
                    "span[@class='price']/a/span[@class='best-price']/text()").extract()[0]
            except IndexError:
                try:
                    item['old_price'] = sel.xpath(
                        "span[@class='price']/a/span[@class='old-price']/text()").extract()[0]
                    item['best_price'] = sel.xpath(
                        "span[@class='price']/a/span[@class='best-price widthC']/text()").extract()[0]
                    item['disc'] = sel.xpath(
                        "span[@class='price']/span[@class='dtoF']/text()").extract()[0]
                except IndexError as error:
                    logger.error(f"Error fetching price: {error}")
                    continue

            # *** Image
            # Skip si no tiene imagen
            try:
                item['image_url'] = sel.xpath(
                    "a[@class='product-image']/img/@src").extract()[0]
            except IndexError as error:
                logger.error(f"Error fetching image href: {error}")
                continue

            # *** URL
            # Skip si no tiene url
            try:
                item['url'] = sel.xpath("a/@href").extract()[0]
            except IndexError as error:
                logger.error(f"Error fetching product URL: {error}")
                continue

            # Abrir cada item para obtener el color y el SKU (tallas)
            driver.find_element_by_tag_name(
                'body').send_keys(Keys.CONTROL + 't')
            driver.get(item['url'])

            # Esperar que cargue el botón de compra para validar que sea una página correcta
            # Skip el producto si no tiene esta información
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//a[@class='buy-button buy-button-ref']")))
            except TimeoutException as error:
                logger.error(f"Error waiting for colors and SKU list: {error}")
                continue

            # Encontrar los colores que no sean unavailable
            colors = driver.find_elements(
                By.XPATH, "//span[@class='group_0']/input[not(contains(@class,'item_unavaliable'))]")

            item['color_sku'] = []
            for color_item in colors:
                driver.execute_script("arguments[0].click();", color_item)
                time.sleep(3)
                itemSelector = Selector(text=driver.page_source)

                # *** Description
                try:
                    item['description'] = itemSelector.xpath(
                        "//div[@class='productDescription']/text()").extract()[0]
                except IndexError as error:
                    logger.error(f"Error fetching description: {error}")

                # *** Reference
                try:
                    item['reference'] = itemSelector.xpath(
                        "//div[contains(@class,'productReference')]/text()").extract()[0]
                except IndexError as error:
                    logger.error(f"Error fetching reference: {error}")

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
                'body').send_keys(Keys.CONTROL + 'w')

            yield item
