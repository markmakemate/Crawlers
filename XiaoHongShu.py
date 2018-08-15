import scrapy
from scrapy.exporters import JsonItemExporter
from scrapy.loader import ItemLoader 
class MyItem(Item):
    name=scrapy.Field()
    follower=scrapy.Field() 
class XiaoHongShu(scrapy.Spider):
    name="Xiaohongshu"
    def __init__(self,category=None,*args,*kwargs):
        super(XiaoHongShu,self).__init__(*args,*kwargs)
        self.allowed_domain=['xianghongshu.com']
        self.start_url='http://www.xiaohongshu.com/explore/?tab=cosmetics'
        self.User=ItemLoader(item=MyItem(),response=response)
    def parse(self,response):
        for url in response.xpath('//a[@class="note-href"]/@href').extract():
            yield scrapy.Request(url,callback=self.parse_items)
        return self.User.load_item()
    def parse_items(self,response):
        self.User.add_xpath('name','//div[@class="right-card"]/a//h6[@class="name"/span/text()]')
        self.User.add_xpath('follower','//div[@class="right-card"]/a//h6[@class="name"/span/text()]')
    def export_items(self,info):
        f=open('/home/user_info/user_info.json','wb')
        export=JsonItemExporter(f)
        export.start_exporting()
        export.export_item(info)
        return export
XiaoHongShu XHS
XHS.export_items(XHS.parse())
XHS.export_items.finish_exporting()



    

