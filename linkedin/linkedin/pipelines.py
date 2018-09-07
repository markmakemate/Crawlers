# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.item import Item
from scrapy.exporters import JsonItemExporter
class LinkedinPipeline(object):
    def __init__(self):
        self.path="/home/markmakemate/文档"
        self.filename="linkedin.json"
        self.f=open('/'.join([self.path,self.filename]),'w')
    def export_items(self,itemloader):
        exporter=JsonItemExporter(self.f)
        exporter.start_exporting()
        exporter.export_item(itemloader)
        return exporter
    def process_item(self, item, spider):
        exporter=self.export_items(item)
        exporter.finish_exporting()
        return item
