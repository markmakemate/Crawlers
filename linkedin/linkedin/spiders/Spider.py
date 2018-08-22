# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader;
from scrapy.item import Item;
class MyItem(Item):
    profile=scrapy.Field()
    name=scrapy.Field()
    job=scrapy.Field()
    city=scrapy.Field()
    Background=scrapy.Field()
    Experience=scrapy.Field()
    Education=scrapy.Field()
    Volunteer_Experience=scrapy.Field()

class ItemProcessor:
    #function process_profile aims to seperate profile item into name,job and city items#
    def process_profile(self,itemloader):
        profile='\n'.join(itemloader['profile'])
        if profile is not ['']:
            self.add_profile(itemloader)
        itemloader.replace_value('profile',profile)
        
    #function process_background aims to seperate the background item into Experience, Education and Volunteer_Experience items#
    def process_background(self,itemloader):
        background='\n'.join(itemloader['Background'])
        itemloader.replace_value('Background',background)
        if background is not ['']:
            self.add_Background(itemloader)
        
    def add_Background(self,itemloader):
        context=itemloader['Background'][0]
        key=['Experience','Education','Volunteer_Experience']
        position=self.KMP(key,context)
        for i in range(len(position)-1):
            if position[i] is not -1:
                begin=position[i]
                p=self.NextPosition(position,i)
                end=position[p]-len(key[p])
                if p is len(position):
                    itemloader.add_value(key[i],context[begin,end])
                    break
                else:
                    itemloader.add_value(key[i],context[begin,end])

    def add_profile(self,itemloader):
        context=itemloader['profile']
        itemloader.add_value('name',context[0])
        itemloader.add_value('job',context[1])
        itemloader.add_value('city',context[2])

    #KMP algorithm can find the position of key in the context#
    #KMP algorithm is a simple but effective string matching algorithm whose complexity is O(m+n),m,n represent the pattern's and string's size respectively#
    #This function is KMP code implement in Python#
    #The return value of KMP is the positions of each key's element last char in context
    def NextPosition(self,position,index):
        for p in range(index+1,len(position)-1):
            if position[p] is not -1:
                break
        return p


class SpiderSpider(scrapy.Spider):
    name = 'Spider'
    allowed_domains = ['linkedin.com']
    start_url='http://www.linkedin.com'
    cookie=[{'name':'_gat','value':'1','domain':'.linkedin.com','path':'/'}]
    Craft=ItemLoader(Item=MyItem())
    home_page='/'.join([start_url,'company','kfc-us'])
    def start_requests(self):
        yield scrapy.FormRequest(self.home_page,cookies=self.cookie,callback=self.parse)
    def parse(self,response):
        Insearch_url=response.xpath('//span[@class="org-company-employees-snackbar__highlight-container description-span"]//a/@href').extract()
        for url in Insearch_url:
            scrapy.Request(url,cookies=self.cookie,callback=self.parse_item)
        return self.Craft.load_item()
    def parse_item(self,response):
        for url in response.xpath('//div[@class="search-results__cluster-content"]/ul[@class="results-list ember-view"]//li//div[@class="search-result__image-wrapper"]/a/@href').extract():
            scrapy.Request(url,cookies=self.cookie,callback=self.parse_page)
    def parse_page(self,response):
        for profile in response.xpath('//div[@class="display-flex align-items-center"]//text()').extract():
            self.Craft.add_value('profile',profile)
        for background in response.xpath('//span[@class="background-details"]//text()').extract():
            self.Craft.add_value('Background',background)


