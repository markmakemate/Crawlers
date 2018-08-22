# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LinkedinItem(scrapy.Item):
    profile=scrapy.Field()
    name=scrapy.Field()
    job=scrapy.Field()
    city=scrapy.Field()
    Background=scrapy.Field()
    Experience=scrapy.Field()
    Education=scrapy.Field()
    Volunteer_Experience=scrapy.Field()
