__author__ = 'py'
# -*- coding: UTF-8 -*-
import sys, os, re, urllib
import smtplib
import time
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def readfile(filename):
    f = open(filename, "r")
    return f.read().encode('utf-8')

def sendmail(subject, msg, toaddrs, fromaddr, smtpaddr, password):
    '''''
    @subject:邮件主题
    @msg:邮件内容
    @toaddrs:收信人的邮箱地址
    @fromaddr:发信人的邮箱地址
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @password:发信人的邮箱密码
    '''
    mail_msg = MIMEMultipart()
    #2.x使用
    #if not isinstance(subject, unicode):
        #subject = unicode(subject, 'utf-8')
    mail_msg['Subject'] = subject
    mail_msg['From'] = fromaddr
    mail_msg['To'] = ';'.join(toaddrs)
    mail_msg.attach(MIMEText(msg, 'plain', 'utf-8'))
    try:
        s = smtplib.SMTP()
        s.connect(smtpaddr)  # 连接smtp服务器
        s.login(fromaddr, password)  # 登录邮箱
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string())  # 发送邮件
        s.quit()
    except Exception as e:
        print("Error: unable to send email")
        print(traceback.format_exc())


if __name__ == '__main__':
    #获取上级目录路径
    parent_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    fromaddr = "xxxx@163.com"
    smtpaddr = "smtp.163.com"
    toaddrs = ["xxxx@163.com"]
    subject = "最近股票相关公告" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    password = "xxxx"
    msg = readfile(parent_path + "/WebCrawler/stock_info/info.txt")
    sendmail(subject, msg, toaddrs, fromaddr, smtpaddr, password)