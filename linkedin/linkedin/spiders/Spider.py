# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.item import Item
import sys
sys.path.append('../')
from items import LinkedinItem
from items import ItemProcessor
from selenium.webdriver import ActionChains as action
from scrapy.exporters import JsonItemExporter
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
class SpiderSpider(scrapy.Spider):
    name = 'Spider'
    allowed_domains = ['linkedin.com']
    start_url='http://www.linkedin.com'
    cookie=[{'name':'_gat','value':'1','domain':'.linkedin.com','path':'/'}]
    Craft=ItemLoader(Item=LinkedinItem())
    def __init__(self,company):
        self.key=company
        self.browser=webdriver.Firefox()
    def start_requests(self):
        yield scrapy.Request(
            url=self.start_url,
            meta={"Selenium":True},
            cookie=self.cookie,
            callback=self.parse
            )
    def parse(self,response):
        driver=webdriver.Firefox()
        driver.get(response.url)
        Insearch_url=response.xpath('//div[@class="display-flex"]//div[@class="search-result_wrapper"]//a/@href').extract()
        for url in Insearch_url:
            if url is not '#':
                scrapy.Request(url,meta={"Selenium":False},cookie=self.cookie,callback=self.parse_page)
        while driver.find_element_by_css_selector('div.next-text') is not None:
            driver.find_element_by_css_selector('div.next-text').click()
            Insearch_url=response.xpath('//div[@class="display-flex"]//div[@class="search-result_wrapper"]//a/@href').extract()
            for url in Insearch_url:
                if url is not '#':
                    scrapy.Request(url,meta={"Selenium":False},cookie=self.cookie,callback=self.parse_page)
        yield self.Craft.load_item()
    def parse_page(self,response):
        for profile in response.xpath('//div[@class="display-flex align-items-center"]//text()').extract():
            self.Craft.add_value('profile',profile)
        for background in response.xpath('//span[@class="background-details"]//text()').extract():
            self.Craft.add_value('Background',background)
    def closed(self,spider):
        print('spider closed')
        self.browser.close()




