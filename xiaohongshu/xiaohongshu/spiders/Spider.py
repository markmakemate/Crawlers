# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.item import Item
#A crawler which can scrape fixed data from 小红書, implementing with the framework Scrapy#
#Loader of Kol's profile#
class KOL_Profile(scrapy.Item):
    name=scrapy.Field()
    follower=scrapy.Field() 
    like_collection=scrapy.Field()
    tag=scrapy.Field()
    url=scrapy.Field()

#Loader of kol's articles#
class KOL_Article(scrapy.Item):
    KOL_name=scrapy.Field()
    tags=scrapy.Field()
    content=scrapy.Field()
    like_number=scrapy.Field()
    star_number=scrapy.Field()
    comment=scrapy.Field()
#Profile data processing#
class Profile:
    def parse_kol_profile(self,response,profile):
        for url in response.xpath('//a[@class="note-href"]/@href').extract():
            scrapy.Request(url,callback=lambda profile:self.kol_profile_parser(profile))
        return profile.load_item()

    #Storage progress#
    def kol_profile_parser(self,response,itemloader):
        profile=itemloader
        profile.add_value('name',response.xpath('//span[@class="name-detail"]/text()').extract())
        profile.add_value('follower',response.xpath('//span[@class="fans"]/text()').extract())
        profile.add_value('like_collection',response.xpath('//span[@class="collect"]/text()').extract())
        profile.add_value('tag',response.xpath('//p[@class="brief"]/text()').extract())
        profile.add_value('url',response.xpath('//a[@class="author-info"]/@href').extract())

#Article's data processing#
class Article:
    def parse_kol_article(self,kol_url):
        yield scrapy.Request(kol_url,callback=self.storeArticle)

    def storeAriticle(self,response):
        itemloader=ItemLoader(item=KOL_Article())
        for url in response.xpath('//a[@class="note-href"]/@href').extract():
            scrapy.Request(url,callback=lambda item=itemloader:self.storage(item))
        return itemloader.load_item()

    #Storage progress#
    def storage(self,response,itemloader):
        for name in response.xpath('//span[@class="name-detail"]/text()').extract():
            itemloader.add_value('KOL_name',name)
        for note in response.xpath('//div[@class="related-tags"]//a/text()').extract():
            itemloader.add_value('tags',note)
        for Content in response.xpath('//p[@class="content"]//p/text()').extract():
            itemloader.add_value('content',Content)
        for like_number in response.xpath('//span[@class="like"]/span/text()').extract():
            itemloader.add_value('like_number',read_number)
        for comment in response.xpath(''):
            itemloader.add_value('comment',comment)
        for star in response.xpath('//span[@class="star"]/span/text()').extract():
            itemloader.add_value('star_number',star)
        getContent(itemloader)
    
    #join "content" list#
    def getContent(self,itemloader):
        text='\n'.join(itemloader['content'])
        itemloader.replace_value('content',text)

#Users can apply the interfaces and configure parameters to crawl the data they want#
#Transaction the data that have been scraped to json file#
class SpiderSpider(scrapy.Spider,Article,Profile):
    name = 'Spider'
    allowed_domains = ['www.xiaohongshu.com/explore']
    def __init__(self,category=None,*args,**kargs):
        super(SpiderSpider,self).__init__(*args,**kargs)
        self.start_urls = ['http://www.xiaohongshu.com/explore?tab=cosmetics']
    def parse(self,response):
        profile=ItemLoader(Item=KOL_Profile())
        kol_profile=super(SpiderSpider,self).parse_kol_profile(response,profile)
        yield kol_profile
    def parse_article(self,kol_url):
        yield super(SpiderSpide,self).parse_kol_article(kol_url)

