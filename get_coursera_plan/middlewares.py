# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
#from scrapy import Response

class GetCourseraPlanSpiderMiddleware(object):
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


class GetCourseraPlanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
        
    options=webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('Cookie=CSRF3-Token=1522410405.bYnBFOkb2KsqSCr5; __204u=6103927981-1521546405475; __204r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Do7xXyWyiJWQW2talU8c8r_TKAey4KyCvc3Ko8ca1rFiuwA7Hbhh4TtBE49hSKsZb%26wd%3D%26eqid%3Dcf60868000053c92000000045ab0f4a1; _ga=GA1.2.377362576.1521546438; CAUTH=ykNsv5Mc4srnSZJZ2zPzk0-ZYNAln58E7KnqgY42PeAd0fIpNA32DqAS4aH5oiYsT4y1jI_Jrd2PWQmPQWEieQ.tjviWKrvZv8jCHvF5pjGfw.NrZK6-Aujo179iKqSTHMK6xB_J61YRONRnDo_AT-kDKLNnwUHmEAGw4WKODlQD9jeWYbFLiDZVpadkF6yXMqs9Ii5Ks1d8CeJ_zZrszk-Eq0Vi9j__lSRYmZ6rokVlar3jq1d6sdqgZX-5C49V2A0ynyNIYOmfdToIMJrxFtBvk; maestro_login_flag=1; _gid=GA1.2.1841576143.1521706165; stc113717=env:1521718993%7C20180422114313%7C20180322121313%7C1%7C1030880:20190322114313|uid:1521546442652.1055449565.6636324.113717.1714164153:20190322114313|srchist:1030879%3A1%3A20180420114722%7C1030880%3A1521718993%3A20180422114313:20190322114313|tsa:1521718993715.2033105959.4947824.6000841186350514.:20180322121313')
    #driver=webdriver.Chrome(options=options,executable_path='C:\\Users\\Helen YU Yu\\Downloads\\chromedriver_win32\\chromedriver.exe')
    driver=webdriver.Chrome(options=options)
    

    def process_request(self, request, spider):
        print("this is url:"+request.url)
        if request.url == "https://www.coursera.org/robots.txt":
            print("this is robot.txt")
            return None
        else:
            if not 'new_handler' in request.meta.keys():
                self.driver.get(request.url)
                print("start sleep")
                time.sleep(30)
                a = input("oversleep")
                if a == "OK":
                    content = self.driver.page_source.encode('utf-8')
                    return HtmlResponse(self.driver.current_url, encoding='utf-8', body=content, request=request)
            else:
                self.driver.get(request.url)
                print("start to get lesson info...")
                time.sleep(30)
                content = self.driver.page_source.encode('utf-8')
                response = HtmlResponse(self.driver.current_url, encoding='utf-8', body=content, request=request)
                response.meta['week_info'] = request.meta['week_info']
                response.meta['deadline'] = request.meta['deadline']
                return response
        
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

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
