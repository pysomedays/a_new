# -*- coding: utf-8 -*-
import urllib
import re
import os
import string
from urllib import FancyURLopener

class MyOpener(FancyURLopener):
    version ='Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2'#可以从firefox help menu中找到相关版本信息
myopener=MyOpener()

file_open = open("fund_list.txt",'r') #fund_list.txt是使用chrome按F12复制dbtable内容得到的，本文数据来源天天基金网
file_read = file_open.read()
fundnumname = r'<input id="chk(.*?)" type="checkbox">'
fundnum_com = re.compile(fundnumname)#输出正则括号里面的内容
fundnumlist = re.findall(fundnum_com, file_read)
print fundnumlist
if os.path.exists('fund_scale.txt'):
    os.remove('fund_scale.txt')
for fundnum in fundnumlist:
    page=myopener.open("http://fund.eastmoney.com/%s.html" %fundnum)

    #page=urllib.urlopen("http://c2.1024mx.pw/pw/htm_data/16/1704/594093.html")
    try:
        html=page.read()
    finally:
        page.close()


    #if os.path.exists('htmltest.txt'):
        #os.remove('htmltest.txt')
    #os.mknod('htmltest.txt')
    file_html = open("htmltest.txt",'w')
    file_html.write(html)

    scalename = r'基金规模</a>：(.+?)（2017'
    scale = re.compile(scalename)#输出正则括号里面的内容

    scalelist = re.findall(scale, html)
    scale_str = ''.join(scalelist)
    print (scale_str)
    x = 0
    #if os.path.exists('fund_scale.txt'):
        #os.remove('fund_scale.txt')
    #os.mknod('fund_scale.txt')
    file_fundscale = open("fund_scale.txt",'a')
    file_fundscale.write('基金代码'+ fundnum + ': ' + scale_str + "\n")