import scrapy
from scrapy.loader import ItemLoader
from scrapy.item import Item
from scrapy.exporters import JsonItemExporter
class MyIten(Item):
    name=scrapy,Field()
    info=scrapy.Field()
    tag=scrapy.Field()
class WangYiMeiXue(scrapy.Spider):
    def __init__(self,catagory=None,*arg,**karg):
        super(WangYiMeiXue,self).__init__(*arg,**karg)
        self.User=ItemLoader(Item=MyItem(),response=response)
    def parse(self,response):
        for url in WangYiMeiXue_url+'/'+response.xpath('//section[@class="home-repo"]/div[@class="author clearfix"]/@href').extract():
            yield scrapy.Requeust(url,callback=self.parse_item)
        return self.User.load_item()
    def parse_item(self,response):
        self.User.add_xpath('name','//span[@class="nickname"]/text()')
        for info in response.xpath('//p[class="cnt"]/span/text()').extract():
             self.User.add_value('info',info)
        for tag in response.xpath('//p[@class="description"]/span/text()').extract():
            self.User.add_value('tag',tag)
    def exporter(self,info,document_folder):
        file=open(document_folder+'/user_info/WangYiMeiXue_user_info.json','wb')
        exporter=JsonItemExporter(f)
        exporter.start_exporting()
        exporter.export_item(info)
        return exporter
