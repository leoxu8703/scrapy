# -*- coding: utf-8 -*-
import MySQLdb as db
from scrapy_example import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyExamplePipeline(object):
    def __init__(self):
        self.connection= db.connect(host=settings.MYSQL_HOST,port=settings.MYSQL_PORT,user=settings.MYSQL_USER,passwd=settings.MYSQL_PASSWORD, db=settings.MYSQL_DB,charset = 'utf8')

    def close_spider(self,spider):
        if hasattr(self, 'connection'):
            self.connection.close()

    def process_item(self, item, spider):
        with self.connection as cur:
            sql="""insert into resource(`title`,`link`,`desc`) values('{0}','{1}','{2}')"""
            sqlnew=sql.format(item['title'],item['link'],item['desc'])
            cur.execute(sqlnew)

