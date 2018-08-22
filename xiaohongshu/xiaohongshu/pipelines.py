# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
class XiaohongshuPipeline(object):
    def __init__(self):
        self.path="D:/Data"
        self.filename="LittleReadBook.json"
        self.file=open('/'.join([self.path,self.filename]),'wb')
    def export_items(self,item):
        export=JsonItemExporter(self.file)
        export.start_exporting()
        export.export_item(item)
        return export
    def process_item(self, item,spider):
        exporter=self.export_items(item)
        exporter.finish_exporting()
        return item
    def close_spider(self,spider):
        self.file.close()
