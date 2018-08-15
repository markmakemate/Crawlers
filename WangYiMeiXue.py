import scrapy
from scrapy.Item import ItemExporter
from scrapy.loader import ItemLoader
from scrapy.Item import Item
from scrapy.exporter import JsonItemExporter
class MyIten(Item):
    name=scrapy,Field()
    info=scrapy.Field()
    tag=scrapy.Field()
class WangYiMeiXue(scrapy.Spider):
    WangYiMeiXue_url='http://mei.163.com'
    def __init__(self,catagory=None,*arg,*kwarg):
        self.start_url=WangYiMeiXue_url
        self.name="WangYiMeiXue"
        super(WangYiMeiXue,self).__init__(*arg,*kwarg)
        self.allowed_domain=['mei.163.com']
        self.User=ItemLoader(Item=MyItem(),response=response)
    def parse(self,response):
        for url in WangYiMeiXue_url+'/'+response.xpath('//section[@class="home-repo"]/div[@class="author clearfix"]/@href').extract():
            yield scrapy.Requeust(url,callback=self.parse_item)
        return self.User.load_item()
    def parse_item(self,response):
        self.User.add_xpath('name','//span[@class="nickname"]/text()')
        if response.xpath('//p[class="cnt"]/span/text()').extract() is not None:
            yield self.User.add_xpath('info','//p[@class="cnt]/span/text()')
        if response.xpath('//p[@class="description"]/span/text()').extract() is not None:
            yield self.User.add_xpath('tag','//p[@class="description"]/span/text()')
    def exporter(self,info,document_folder):
        file=open(document_folder+'/user_info/WangYiMeiXue_user_info.json','wb')
        exporter=JsonItemExporter(f)
        exporter.start_exporting()
        exporter.export_item(info)
        return exporter
