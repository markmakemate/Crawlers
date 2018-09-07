# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader

class LinkedinItem(scrapy.Item):
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
