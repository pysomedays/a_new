# -*- coding: utf-8 -*-
import urllib
import re
import os
from urllib import FancyURLopener

class MyOpener(FancyURLopener):
    version ='Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2'#可以从firefox help menu中找到相关版本信息
myopener=MyOpener()
page=myopener.open("http://www.baidu.com")
n = 4

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent


#page=urllib.urlopen("http://c2.1024mx.pw/pw/htm_data/16/1704/594093.html")
try:
    html=page.read()
finally:
    page.close()


if os.path.exists('htmltest.txt'):
    os.remove('htmltest.txt')
os.mknod('htmltest.txt')
file_html = open("htmltest.txt",'w')
file_html.write(html)

imgname = r'src="(.+?\.jpg)"'
imgre = re.compile(imgname)#输出正则括号里面的内容

imglist = re.findall(imgre, html)
print imglist
x = 0
if not os.path.exists('E:/movie/photos2/%s' %n):
    os.mkdir('E:/movie/photos2/%s' %n)

for imgurl in imglist:
    try:
        #pass
        os.remove('E:/movie/photos2/%s/%s_%s.jpg' %(n,n,x))
    finally:
        pass
    imgopener = MyOpener()
        #print (dir(imgopener))
    imgpage=imgopener.open(imgurl)
    try:
        imgopener.retrieve(imgurl, filename='E:/movie/photos2/%s/%s_%s.jpg' %(n,n,x), reporthook=callbackfunc)
    finally:
        pass
    x += 1
#print html

#htmlfile=urllib.urlretrieve('http://www.baidu.com',filename='htmltest.txt')