import requests
url='http://120.76.205.241:8000/post/xiaohongshu?kw=%E6%9E%97%E5%85%81&apikey=CaSJtEphMgD2jbkFoqXn3sVC68KNd5nWyD8TYshthvyi90VeOmJnTTR7BZeSgmXI'
if __name__ =="__main__":
    r=requests.get(url)
    obj=r.json()
    print(obj)

