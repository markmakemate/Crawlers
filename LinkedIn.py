import scrapy
from scrapy.exporter import JsonItemExporter;
from scrapy.loader import ItemLoader;
from scrapy.Item import Item;
class MyItem(Item):
    name=scrapy.Field()
    job=scrapy.Field()
    City=scrapy.Field()
class LinkedIn(scrapy.Spider):
    Linkedin_url='http://www.linkedin.com'
    def __init__(self,category=None,*arg,*kwarg,company):
        super(LinkedIn,self).__init__(*arg,*kwarg)
        self.start_url='%s%s%s'%[Linkedin_url,'/company/',company]
        self.name="LinkedIn"
        self.Craft=ItemLoader(Item=MyItem(),response=response)
    def parse(self,response):
        Inserch_url=reponse.xpath('//a[@class="org-company-employees\w+"]/@href').extract()
        cookie=[{'name':'_gat','value':'1','domain':'.linkedin.com','path':'/'}]
        for url in Insearch_url:
            yield scrapy.Request(url,cookies=cookie,callback=self.parse_item)
        i=1
        for url in '%s%s%s'%(self.Insearch_url,'&page',byte(i)):
            if "illustrated \w+ neterror" is not in response.xpath('body/@class').extract():
                yield scrapy.Request(url,cookies=cookie,callback=self.parse_item)
                i=i+1
        return self.Craft.load_item()
    def parse_item(self,response):
        self.Craft.add_xpath('name','//span[@class="name actor-name"]/text()')
        self.Craft.add_xpath('job','//p[@class="subline-level-1\w+"/text()')
        self.Craft.add_xpath('City','//p[@class="subline-level-2\w+"/text()')
    def exporter(self,info,document_folder):
        f=open(document_folder+'/Craft_info/craft_info.json','wb')
        exporter=JsonItemExporter(f)
        exporter.start_exporting()
        exporter.export_item(info)
        return exporter
LinkedIn L
L.exporter(L.parse())
L.exporter.finish_exporting()

