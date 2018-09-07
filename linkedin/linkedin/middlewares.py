# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http.response.html import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains as action
import time

class LinkedinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LinkedinDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(
            timeout=crawler.Crawler.settings.get("TIMEOUT"),
            height=crawler.Crawler.settings.get("WINDOW_HEIGHT"),
            width=crawler.Crawler.settings.get("WINDOW_WIDTH"),
            isLoadImage=crawler.Crawler.settings.get("LOAD_IMAGE")
        )
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    def __init__(self,timeout,height,width,isLoadImage,*args, **kwargs):
        self.timeout=timeout
        self.height=height
        self.width=width
        self.isLoadImage=isLoadImage
        super(LinkedinDownloaderMiddleware,self).__init__(*args,**kwargs)
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        selenium=request.meta.get("Selenium")
        spider.browser.set_page_load_timeout(self.timeout)
        spider.browser.set_window_size(self.width,self.height)
        if selenium:
            try:
                spider.browser.get(request.url)
                _input=wait.WebDriverWait.until(self=wait.WebDriverWait,method=ec.presence_of_element_located((By.XPATH,'//div[@class="nav-search-typehead"]//input')))
                time.sleep(2)
                _input.clear()
                _input.send_keys(spider.key)
                _input.send_keys(Keys.RETURN)
                action.click(self=action,on_element=(By.CSS_SELECTOR,'strong'))
                body=wait.WebDriverWait.until(
                    self=wait.WebDriverWait,method=ec.presence_of_element_located((By.XPATH,'//div[@class="ember-view"]'))
                )
            except Exception as e:
                print('Exception is %s')%e
                return HtmlResponse(url=request.url,request=request)
            else:
                time.sleep(3)
                return HtmlResponse(url=request.url,body=body,request=request)
        else:
            time.sleep(3)
            body=wait.WebDriverWait.until(
                self=wait.WebDriverWait,method=ec.presence_of_element_located((By.XPATH,'//div[@class="ember-view"]/*'))
            )
            return HtmlResponse(url=request.url,body=body,request=request)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
