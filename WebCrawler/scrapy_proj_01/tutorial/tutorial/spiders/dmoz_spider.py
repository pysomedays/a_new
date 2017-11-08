# -*- coding:utf-8 -*-
import scrapy
import re, urllib, os
from bs4 import BeautifulSoup
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://www.3dmgame.com/"]
    # start_urls = ['http://www.baidu.com/s?q=&tn=baidulocal&ct=2097152&si=&ie=utf-8&cl=3&wd=seo%E5%9F%B9%E8%AE%AD']

    start_urls = []

    #获取上级目录路径
    parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    words = open(parent_path + "/words.txt")
    for word in words:
        word = word.strip()
        url = 'http://so.3dmgame.com/?type=0&keyword=%s' % urllib.parse.quote(word)
        start_urls.append(url)

        def __get_url_query(self, url):
            m = re.search("wd=(.*)", url).group(1)
            return m

        def parse(self, response):
            n = 0
            print("我的")
            for sel in response.xpath('//td'):
                print("我的" + sel)
                item = DmozItem()
                query = urllib.parse.unquote(self.__get_url_query(response.url))
                title = re.sub('<[^>]*?>','',sel.xpath('.//a/font[@size="3"]').extract()[0])
                lading = sel.xpath('.//a[1]/@href').extract()[0]
                time = sel.xpath('.//font[@color="#008000"]/text()').re('(\d{4}-\d{1,2}-\d{1,2})')[0]
                size = sel.xpath('.//font[@color="#008000"]/text()').re('(\d+K)')[0]

                n += 1
                item['rank'] = n
                item['title'] = title.encode('utf8')
                item['lading'] = lading.encode('utf8')
                item['time'] = time.encode('utf8')
                item['size'] = size.encode('utf8')
                item['query'] = query

                yield item
    # just for test
    # print("我的" + str(start_urls))