import scrapy
from scrapy.exporter import JsonItemExporter;
from scrapy.loader import ItemLoader;
from scrapy.Item import Item;
import ctypes
class MyItem(Item):
    profile=scrapy.Field()
    name=scrpay.Field()
    job=scrapy.Field()
    city=scrapy.Field()
    Background=scrapy.Field()
    Experience=scrapy.Field()
    Education=scrapy.Field()
    Volunteer_Experience.Field()

class ItemProcessing:
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
    #The return value of KMP is the positions of each key's element last char in context#
    def KMP(self,key,context):
    
    def NextPosition(self,position,index):
        for p in range(index+1,len(position)-1):
            if position[p] is not -1:
                break
        return p

class LinkedIn(scrapy.Spider,ItemProcessing):
    Linkedin_url='http://www.linkedin.com'
    cookie=[{'name':'_gat','value':'1','domain':'.linkedin.com','path':'/'}]
    def __init__(self,category=None,*arg,*kwarg,company):
        super(LinkedIn,scrapy.Spider).__init__(*arg,*kwarg)
        self.start_url='%s%s%s'%[Linkedin_url,'/company/',company]
        self.name="LinkedIn"
        self.Craft=ItemLoader(Item=MyItem(),response=response)

    def parse(self,response):
        Inserch_url=reponse.xpath('//span[@class="org-company-employees-snackbar__highlight-container description-span"]//a/@href').extract()
        for url in Insearch_url:
            yield scrapy.Request(url,cookies=cookie,callback=self.parse_item)
        i=2
        for url is '%s%s%s'%(self.Insearch_url,'&page',byte(i)):
            if "illustrated \w+ neterror" is not in response.xpath('body/@class').extract():
                if url is not '#':
                    yield scrapy.Request(url,cookies=cookie,callback=self.parse_item)
                i=i+1
        return self.Craft.load_item()
    def parse_item(self,response):
        for url in response.xpath('//div[@class="search-results__cluster-content"]/ul[@class="results-list ember-view"]//li//div[@class="search-result__image-wrapper"]/a/@href').extract():
            yield scrapy.Request(url,cookies=cookie,callback=self.parse_page)
        return self.Craft

    def parse_page(self,response):
        for profile in response.xpath('//div[@class="display-flex align-items-center"]//text()').extract():
            self.Craft.add_value('profile',profile)
        for background in response.xpath('//span[@class="background-details"]//text()').extract():
            self.Craft.add_value('Background',background)
        super(LinkedIn,ItemProcessing).process_background(Craft)
        super(LinkedIn,ItemProcessing).process_profile(Craft)

    def exporter(self,itemloader,path,file_name):
        f=open('/'.join([path,file_name]),'wb')
        exporter=JsonItemExporter(f)
        exporter.start_exporting()
        exporter.export_item(itemloader)
        return exporter

