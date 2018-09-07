# -*- coding: utf-8 -*-
import scrapy
import sys
from scrapy.loader import ItemLoader
from scrapy.item import Item
sys.path.append("..")
from items import MyItem
from items import ItemProcessor
class SpiderSpider(scrapy.Spider):
    name = 'Spider'
    allowed_domains = ['mei.163.com']
    def __init__(self,catagory=None,*arg,**karg):
        super(SpiderSpider,self).__init__(*arg,**karg)
        self.start_url = ['http://mei.163.com/']
    def parse(self,response):
        User=ItemLoader(Item=MyItem(),response=response)
        processor=ItemProcessor(User)
        for url in ''.join([self.start_url,'/',response.xpath('//section[@class="home-repo"]/div[@class="author clearfix"]/@href').extract()]):
            scrapy.Request(url,callback=processor.parse_item)
        return User.load_item()
    

