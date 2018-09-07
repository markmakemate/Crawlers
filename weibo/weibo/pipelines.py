# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exporters import JsonItemExporter


class WeiboPipeline(object):
    def __init__(self):
        self.path='/home/文档'
        self.document="weibo.json"
    def export_items(self,item):
        with open('/'.join([self.path,self.document]),'w+') as f:
            exporter=JsonItemExporter(f)
            exporter.start_exporting()
            exporter.export_item(item)
            f.close()
    def process_item(self, item, spider):
        self.export_items(item)
        return item