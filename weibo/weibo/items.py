# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader

class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content=scrapy.Field()
    pass
class ItemProcessor:
    def __init__(self,item):
        self.container=item
    def parse_content(self,response):
        for content in response.xpath('//div[@class="WB_frame"]//div[@id="Pl_Office_MyProfileFeed__21"]//text()'):
            self.container.add_value('content',content)