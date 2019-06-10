# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
#
# class ImoocPipeline(object):
#     def process_item(self, item, spider):
#         return item


#########################
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#encoding=utf8
import json
from twisted.enterprise import adbapi
from scrapy import log

import pymysql
import pymysql.cursors
import codecs
import copy

class ImoocPipeline(object):
    def __init__(self):
        self.file = codecs.open('imooc.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MySQLPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("pymysql",
                                           db = "imooc",            # 数据库名
                                           user = "root",       # 数据库用户名
                                           passwd = "123456",     # 密码
                                           cursorclass = pymysql.cursors.DictCursor,
                                           charset = "utf8",
                                           use_unicode = True
                                           )
    def process_item(self, item, spider):
        asynItem=copy.deepcopy(item)
        query = self.dbpool.runInteraction(self._conditional_insert,asynItem)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tb, item):
        tb.execute(""" insert into imooc_info5 (title,substance,level,sums) values (%s,%s,%s,%s)""",(item['Course_name'],item['Course_content'],item['Course_level'],item['Course_attendance']))
        tb.execute("""commit""")
        log.msg("Item data in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)