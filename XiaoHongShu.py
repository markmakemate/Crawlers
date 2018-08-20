import scrapy
import mysql.connector
import mysql.cursor
import json
import nltk #A NLP library, I plan to apply it to analyse articles#
from scrapy.exporters import JsonItemExporter
from scrapy.loader import ItemLoader
#A crawler which can scrape fixed data from 小红書, implementing with the framework Scrapy#

#Loader of Kol's profile#
class KOL_Profile(Item):
    name=scrapy.Field()
    follower=scrapy.Field() 
    like&collection=scrapy.Field()
    tag=scrapy.Field()
    url=scrapy.Field()

#Loader of kol's articles#
class KOL_Article(Item):
    KOL_name=scrapy.Field()
    tags=scrapy.Field()
    content=scrapy.Field()
    like_number=scrapy.Field()
    star_number=scrapy.Field()
    comment=scrapy.Field()

#Profile data processing#
class Profile:
    def parse_kol_profile(self,response):
        Profile=ItemLoader(item=KOL_Profile(),response=response)
        for url in response.xpath('//a[@class="note-href"]/@href').extract():
            yield scrapy.Request(url,callback=self.kol_profile_parser(Profile))
        return Profile

    #Storage progress#
    def kol_profile_parser(self,response,itemloader):
        Profile=itemloader
        Profile.add_xpath('name','//span[@class="name-detail"]/text()')
        Profile.add_xpath('follower','//span[@class="fans"]/text()')
        Profile.add_xpath('like&collection','//span[@class="collect"]/text()')
        Profile.add_xpath('tag','//p[@class="brief"]/text()')
        Profile.add_xpath('url','//a[@class=author-info]/@href')

#Article's data processing#
class Article:
    def parse_kol_article(self,kol_url):
        yield scrapy.Request(kol_url,callback=self.storeArticle)

    def storeAriticle(self,response):
        itemloader=ItemLoader(item=KOL_Article(),response=response)
        for url in response.xpath('//a[@class="note-href"]/@href').extract():
            yield scrapy.Request(url,callback=self.storage(itemloader))
        return itemloader.load_item()

    #Storage progress#
    def storage(self,response,itemloader):
        for name in response.xpath('//span[@class="name-detail"]/text()').extract():
            itemloader.add_value('KOL_name',name)
        for note in response.xpath('//div[@class="related-tags"]//a/text()').extract():
            itemloader.add_value('tags',note)
        for Content in response.xpath('//p[@class="content"]//p/text()').extract():
            itemloader.add_value('content',Content)
        for read_number in response.xpath('//'):
            itemloader.add_value('read_number',read_number)
        for like_number in response.xpath('//span[@class="like"]/span/text()').extract():
            itemloader.add_value('like_number',read_number)
        for comment in response.xpath(''):
            itemloader.add_value('comment',comment)
        for star in response.xpath('//span[@class="star"]/span/text()').extract():
            itemloader.add_value('star_number',star)
        getContent(itemloader)
    
    #join "content" list#
    def getContent(self,itemloader):
        text='\n'.join(itemloader['content'])
        itemloader.replace_value('content',text)

#Users can apply the interfaces and configure parameters to crawl the data they want#
#Transaction the data that have been scraped to json file#
class XiaoHongShu(scrapy.Spider,Article,Profile):
    name="XiaoHongShu"
    allowed_domain=['.xiaohongshu.com']

    #Constructor,tab parameter is what u wanna crawl#
    def __init__(self,tab,catagory=None,*arg,*kwarg):
        super(XiaoHongShu,scrapy.Spider).__init__(*arg,*kwarg)
        self.start_url='%s%s%s'%('http://www.xiaohongshu.com/explore','?tab=',tab)
    def parse(self,response):
        yield super(XiaoHongShu,Profile).parse_kol_profile(response)
    def parse_article(self,kol_url):
        yield super(XiaoHongShu,Article).parse_kol_article(kol_url)
    def export_items(self,info,path,file_name):
        f=open('/'.join([path,file_name]),'wb')
        export=JsonItemExporter(f)
        export.start_exporting()
        export.export_item(info)
        return export




#Modeling data#
class Modeling:





    

