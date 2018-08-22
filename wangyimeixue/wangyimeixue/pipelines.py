# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WangyimeixuePipeline(object):
    def __init__(self):
        self.path="D:\Data"
        self.filename="WangYiMeiXue.json"
        self.file=open('/'.join([self.path,self.filename]),'wb')
    def exporter(self,item):
        exporter=JsonItemExporter(self.file)
        exporter.start_exporting()
        exporter.export_item(item)
        return exporter
    def process_item(self, item, spider):
        export=self.exporter(item)
        export.finish_exporting()
        return item
