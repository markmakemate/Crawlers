# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

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
