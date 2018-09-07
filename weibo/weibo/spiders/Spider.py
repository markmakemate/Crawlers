# -*- coding: utf-8 -*-
import scrapy
import sys
from scrapy.item import Item
from scrapy.loader import ItemLoader
from selenium.webdriver import firefox
from selenium import webdriver
sys.path.append('../')
from items import Item
from items import WeiboItem
class SpiderSpider(scrapy.Spider):
    name = 'Spider'
    allowed_domains = ['weibo.com']
    cookie=['SINAGLOBAL=4644087797659.187.1535337310656; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhxOTwU9k-LnM7LcFaObyZO5JpX5KMhUgL.Fo-4e0-cSKBXSh.2dJLoIXnLxK-LBKBLBK.LxKML1-eL1-qLxK-L12qLB-qLxKML1hnLBo2LxKML1-2L1hBLxKnL1KeL1-BLxK-LB-BLBK.LxK-LB-BL1K5t; UOR=,,vga.zol.com.cn; _s_tentry=-; Apache=5549812119704.367.1535945695319; ULV=1535945695521:2:1:1:5549812119704.367.1535945695319:1535337310840; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; ALF=1567504272; SSOLoginState=1535968272; SCF=Atf98wfXbN6QoIL8sjE7cwXHrUjFJGUi1ZOZGHpPYvixqAMq2dakZ7dvdGq5MU3ZLoMbQcQCzA01CW9Gvzh2V9g.; SUB=_2A252iXRADeRhGeNH6FcX9SrIzzWIHXVV_-KIrDV8PUNbmtAKLVHgkW9NStCEUUwTmVLEHhlFVeVPZekxtWkzCzF3; SUHB=02MfNOufHL6his; wvr=6; TC-V5-G0=5fc1edb622413480f88ccd36a41ee587; TC-Page-G0=4e714161a27175839f5a8e7411c8b98c; wb_view_log_5935654449=1920*10801']
    browser=webdriver.Firefox()
    def start_requests(self,index):
        for url in index:
            scrapy.Request(url,meta={'Slenium':True},cookie=self.cookie,callback=self.parse)
    def parse(self, response):
        container=WeiboItem()

        


