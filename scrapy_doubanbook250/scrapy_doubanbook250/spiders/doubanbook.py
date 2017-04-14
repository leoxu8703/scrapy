# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import scrapy
from scrapy_doubanbook250.items import  ScrapyDoubanbook250Item


class DoubanbookSpider(scrapy.Spider):
    name = "doubanbook"
    start_urls = ['https://book.douban.com/top250/']

    def parse(self, response):
        books=response.xpath('//*[@id="content"]/div/div[1]/div/table')
        for book in books:
            item=ScrapyDoubanbook250Item()
            item['cname']=book.xpath('.//div[1]/a/@title').extract()[0]
            info=book.xpath('.//p/text()').extract()[0].split('/')
            if book.xpath('.//div[1]/span/text()').extract():
                item['ename']=book.xpath('.//div[1]/span/text()').extract()[0]
                item['eauthor']=info[0]
                item['publish']=info[-3]
                item['publishtime']=info[-2]
                item['price']=info[-1]
            else:
                item['ename']='没有英文名字'
                item['eauthor']=info[0]
                item['publish']=info[-3]
                item['publishtime']=info[-2]
                item['price']=info[-1]



            if book.xpath('.//div[1]/img/@title').extract():
                item['isread']=book.xpath('.//div[1]/img/@title').extract()[0]
            else:
                item['isread']='不可在线阅读'

            item['booklink']=book.xpath('.//div[1]/a/@href').extract()[0]
            item['rating_num']=book.xpath('.//div[2]/span/text()').extract()[0] 
            item['evaluation']=book.xpath('.//div[2]/span/text()').extract()[1].split()[1][:-3]
            if book.xpath('.//p/span/text()').extract():
                item['comment']=book.xpath('.//p/span/text()').extract()[0]
            else:
                item['comment']='此书没有简短的评语'
            yield item
        
        try:
            next_page=response.xpath('//*[@id="content"]/div/div[1]/div/div/span[3]/a/@href').extract()[0]       
            yield scrapy.Request(next_page, callback=self.parse)
        except:
            pass

