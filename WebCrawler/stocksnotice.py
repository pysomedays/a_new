__author__ = 'sks'
# -*- coding:utf-8 -*-

import urllib
import re
import os
from urllib.request import FancyURLopener

ERRORMSG = u'页面打不开'

class MyOpener(FancyURLopener):
    version ='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'#可以从firefox help menu中找到相关版本信息

# 抓取
class Spider:
    # 页面初始化
    def __init__(self):
        self.siteURL = 'http://data.eastmoney.com/notices/hsa/'
        #self.tool = tool.Tool()

    def pageUrl(self, pageIndex):
        origin_url = self.siteURL
        url = origin_url + str(pageIndex) + '.html'
        return url
    # 获取索引页面的内容
    def getPage(self, pageIndex):
        url = self.pageUrl(pageIndex)
        myopener = MyOpener()
        response = myopener.open(url)
        return response.read().decode('gbk')


    #打印索引页面内容
    def printPage(self, pageIndex):
        page = self.getPage(pageIndex)
        print(page)

    # 获取索引界面stock的信息，list格式
    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('"NOTICETITLE":"(.*?)","INFOCODE".*?"SECURITYCODE":"(.*?)","SECURITYFULLNAME".*?"EUTIME":"(.*?)".*?"Url":"(.*?)"},', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            if ('复牌' in item[0]) or ('收购' in item[0]) or ('股权转让' in item[0]):
                contents.append([item[0], item[1], item[2], item[3]])
        return contents

    def printContents(self, pageIndex):
        contents = self.getContents(pageIndex)
        print(contents)

    # 获取股票公告详情页面
    def getDetailPage(self, infoURL):
        myopener = MyOpener()
        response = myopener.open(infoURL)
        #print(infoURL)
        try:
            if response.read():
                print(infoURL, response.read())
                return response.read().decode('gbk')
        except ValueError:
            print(u'错误：%s' %ERRORMSG)
            return ERRORMSG

    def getNotice(self, page):
        pattern = re.compile('<div class="detail-body" style=".*?">.*?<div style=".*?">(.*?)</div>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1)
        else:
            return ERRORMSG

    # 保存股票公告信息
    def saveNotice(self, content, stockcode, time):
        fileName = "stock_info" + "/" + stockcode + "-" + time[:10] + ".txt"
        f = open(fileName, "w+")
        print(u"正在保存股票信息为", fileName)
        f.write(content)
        f.close()

    # 创建新目录
    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print(u"新建了名字叫做", path, u'的文件夹')
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(u"名为", path, '的文件夹已经创建成功')
            return False

    # 将一页股票信息保存起来
    def savePageInfo(self, pageIndex):
        #self.mkdir(str(pageIndex))
        self.mkdir('stock_info')
        # 获取第一页股票列表
        info = []
        contents = self.getContents(pageIndex)
        for item in contents:
            # item[0]公告标题,item[1]股票代码,item[2]时间,item[3]详细url
            tmpinfo = u"代码为" + item[1] + u"的股票在" + item[2][:10] + u"有公告：" + item[0]
            print(tmpinfo)
            info.append([tmpinfo])
            print(u"保存", item[1], "的信息")
            # 股票详情页面的URL
            # print(item[3])
            detailURL = item[3]
            # 得到股票详情页面代码
            detailPage = self.getDetailPage(detailURL)
            notice = self.getNotice(detailPage)

            # 保存详情页面
            self.saveNotice(notice, item[1], item[2])
        # 记录info信息至文件
        fileName = "stock_info/info.txt"
        f = open(fileName, "w")
        for infoitem in info:
            f.write('    ')
            f.write(str(infoitem) + '\n')
        f.close()


    # 传入起止页码，获取MM图片
    def savePagesInfo(self, start, end):
        for i in range(start, end + 1):
            print(u"正在寻找第", i, u"个页面")
            self.savePageInfo(i)


# 传入起止页码即可，在此传入了1,表示抓取第1页的股票
spider = Spider()
#spider.printPage(1)
#spider.printContents(1)
spider.savePagesInfo(1,6)