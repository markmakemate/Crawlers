# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
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
        for url in response.xpath('//div[@class="note-handle"]/div[@class="comment"]/div[@class="photo"]/a/@href').extract():
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
