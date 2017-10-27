import sys, re
from handlers import *
from util import *
from rules import *

class Parser:
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)
    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler) #每种过滤器都用一遍
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler) #可以理解为每个块用一种规则处理，处理完如果是通用规则则跳出循环，列表规则是对多个块处理所以不同
                    if last:
                        break
        self.handler.end('document')

class BasicTextParser(Parser): #要改变只需要改这里，通用的解释器是超类
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z/]+@[\.a-zA-Z/]+[a-zA-Z/]+)', 'mail')
        self.addFilter(r'\#(.+?)\#', 'img')
        self.addFilter(r'\$\$(.+?)\$\$', 'video')

handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
