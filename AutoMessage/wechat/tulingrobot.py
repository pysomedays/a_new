#coding=utf8
__author__ = 'Peter'
import requests


KEY = '28ad430163fd4c65875bdc6c2d68ec47'

def get_response(msg):
    # 这里构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : '我是大宝宝-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        if r.get('list'):
            return r.get('text') + r.get('list')
        elif r.get('url'):
            return r.get('text') + r.get('url')
        else:
            return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return