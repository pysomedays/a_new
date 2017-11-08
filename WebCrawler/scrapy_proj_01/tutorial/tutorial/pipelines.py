# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLTutorialPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
        host=settings['MYSQL_HOST'],
        db=settings['MYSQL_DBNAME'],
        user=settings['MYSQL_USER'],
        passwd=settings['MYSQL_PASSWD'],
        charset='utf8',
        cursorclass = MySQLdb.cursors.DictCursor,
        use_unicode= True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    #pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    #将每行更新或写入数据库中
    def _do_upinsert(self, conn, item, spider):
        conn.execute(""" INSERT INTO baidu_pc_rank VALUES ('%s','%s','%s','%s','%s','%s') """ % (item['rank'],item['title'],item['lading'],item['time'],item['size'],item['query']))

    #获取url的md5编码
    def _get_linkmd5id(self, item):
        #url进行md5处理，为避免重复采集设计
        return hashlib.md5(item['address']).hexdigest()
    #异常处理
    def _handle_error(self, failure, item, spider):
        log.err(failure)


class FileTutorialPipeline(object):

    def open_spider(self, spider):
        self.file = open('tutorial/datafile/data.txt', 'w') #项目根目录为默认路径

    def close_spider(self, spider):
        self.file.close()

    #pipeline默认调用
    def process_item(self, item, spider):
        line = str(dict(item)) + '\n'
        self.file.write(line)
        self._do_print()
        return item

    #将每行更新或写入数据库中
    def _do_print(self, item, spider):
        print(""" INSERT INTO baidu_pc_rank VALUES ('%s','%s','%s','%s','%s','%s') """ % (item['rank'],item['title'],item['lading'],item['time'],item['size'],item['query']))

    #获取url的md5编码
    def _get_linkmd5id(self, item):
        #url进行md5处理，为避免重复采集设计
        return hashlib.md5(item['address']).hexdigest()
    #异常处理
    def _handle_error(self, failure, item, spider):
        log.err(failure)