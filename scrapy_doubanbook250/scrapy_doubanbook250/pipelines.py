# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import MySQLdb as db
from scrapy_doubanbook250 import settings


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyDoubanbook250Pipeline(object):
    def __init__(self):
        self.connection= db.connect(host=settings.MYSQL_HOST,port=settings.MYSQL_PORT,user=settings.MYSQL_USER,passwd=settings.MYSQL_PASSWORD, db=settings.MYSQL_DB,charset = 'utf8')

    def close_spider(self,spider):
        if hasattr(self, 'connection'):
            self.connection.close()

    def process_item(self, item, spider):
        with self.connection as cur:
            sql="""insert into book values('{0}',"{1}",'{2}','{3}','{4}','{5}','{6}','{7}',{8},'{9}','{10}')""".format(item['cname'],item['ename'],item['isread'],item['booklink'],item['eauthor'],item['publish'],item['publishtime'],item['price'],item['rating_num'],item['evaluation'],item['comment'])
            #print(item['ename'])
            #print(sql)
            cur.execute(sql)

