#encoding: utf-8
import requests
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")
class xiaohongshu:
    def __init__(self,url):
        self.headers={
            "Accept-Encoding":"gzip",
            "Connection":"close"
        }
        self.domain=url
        self.result=dict()
        self.page=0
        self.url=None
    def request(self,**kwargs):
        params=kwargs
        parameter=''
        for key,value in params.items():
            parameter='&'.join(['='.join([key,value]),parameter])
        self.url='?'.join([self.domain,parameter])
        r=requests.get(self.url,headers=self.headers)
        time.sleep(1)
        self.parse_comments(response=r)
    def parse_comments(self,response,path='/home/markmakemate/Documents',name='comment.txt'):
        self.page=self.page+1
        obj=response.json()
        print(self.page)
        print '\n'
        print(obj['data'])
        try:
            if obj['pageToken'] is not None:
                url='&'.join([self.url,'='.join(['pageToken',obj['pageToken']])])
                time.sleep(1)
                r=requests.get(url,headers=self.headers)
                self.parse_comments(response=r)
        except:
            time.sleep(6)
            if obj['pageToken'] is not None:
                url='&'.join([self.url,'='.join(['pageToken',obj['pageToken']])])
                time.sleep(1)
                r=requests.get(url,headers=self.headers)
                self.parse_comments(response=r)
        
if __name__ =="__main__":
    XHS=xiaohongshu('http://120.76.205.241:8000/comment/xiaohongshu')
    XHS.request(apikey='CaSJtEphMgD2jbkFoqXn3sVC68KNd5nWyD8TYshthvyi90VeOmJnTTR7BZeSgmXI',catid='5b879df907ef1c64a2986b02')
    