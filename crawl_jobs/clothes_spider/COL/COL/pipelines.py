# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import re


class ColPipeline:
    def process_item(self, item, spider):
        return item


class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta.get('item')
        image_name = item['uuid'] + '-' + item['reference'] + '.' + (re.search(
            "(.*).(jpg|png|gif|jpeg|tif|tiff|bmp)", request.url).group(0)).split('/')[-1].split('.')[-1]
        file_name = "{0}/{1}".format(item['store'], image_name)
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('The picture is not downloaded well')
        return item

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})
