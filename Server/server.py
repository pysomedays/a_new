#-*- coding:utf-8 -*-

import socket

from http import server
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler #多线程

class Server(ThreadingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write(bytes('Thank you for connecting', encoding = "utf8"))

class  RequestHandler(server.BaseHTTPRequestHandler):
    # 页面模板
    Page = open('pages_inserver\\test_output.html','r').read().encode('utf-8')
    # 处理一个GET请求
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=UTF-8") #响应头部
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)

if __name__ == '__main__':
    #server = Server(('', 1234), Handler)
    server = Server(('', 1234), RequestHandler)
    host = socket.gethostname()
    print(socket.gethostbyname(host))
    server.serve_forever()
'''      
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    #print(dir(c))
    c.send(bytes('Thank you for connecting', encoding = "utf8")) #必须转换为bytes
    c.close()
'''