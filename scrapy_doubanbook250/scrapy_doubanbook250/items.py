# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDoubanbook250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cname= scrapy.Field()
    ename= scrapy.Field()
    isread=scrapy.Field()
    booklink=scrapy.Field()
    eauthor=scrapy.Field()
    publish=scrapy.Field()
    publishtime=scrapy.Field()
    price=scrapy.Field()
    rating_num=scrapy.Field()
    evaluation=scrapy.Field()
    comment=scrapy.Field()    
