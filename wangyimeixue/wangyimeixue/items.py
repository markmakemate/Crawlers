# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.item import Item
from scrapy.exporters import JsonItemExporter
class MyItem(Item):
    name=scrapy.Field()
    info=scrapy.Field()
    tag=scrapy.Field()
class ItemProcessor:
    def __init__(self,User):
        self.User=User
    def parse_item(self,response):
        self.User.add_xpath('name','//span[@class="nickname"]/text()')
        for info in response.xpath('//p[class="cnt"]/span/text()').extract():
             self.User.add_value('info',info)
        for tag in response.xpath('//p[@class="description"]/span/text()').extract():
            self.User.add_value('tag',tag)
