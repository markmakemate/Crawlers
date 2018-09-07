# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.item import Item
from selenium import webdriver
import sys
sys.path.append('../')
from items import KOL_Article
from items import KOL_Profile
from items import Profile
from items import Article
#A crawler which can scrape fixed data from 小红書, implementing with the framework Scrapy#
#Users can apply the interfaces and configure parameters to crawl the data they want#
#Transaction the data that have been scraped to json file#
class SpiderSpider(scrapy.Spider,Article,Profile):
    name = 'Spider'
    allowed_domains = ['www.xiaohongshu.com/explore']
    start_urls = ['http://www.xiaohongshu.com/explore?tab=cosmetics']
    browser=webdriver.Firefox()
    def start_request(self):
        yield scrapy.Request(self.start_url,meta={'Selenium':True},callback=self.parse)
    def parse(self,response):
        profile=ItemLoader(Item=KOL_Profile())
        kol_profile=lambda pro=profile:super(SpiderSpider,self).parse_kol_profile(response,pro)
        yield kol_profile
    def parse_article(self,kol_url):
        yield lambda url=kol_url:super(SpiderSpide,self).parse_kol_article(url)

