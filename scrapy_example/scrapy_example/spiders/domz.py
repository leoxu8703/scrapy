# -*- coding: utf-8 -*-
import scrapy
from scrapy_example.items import ScrapyExampleItem


class DomzSpider(scrapy.Spider):
    name = "domz"
    allowed_domains = ["domztools.net"]
    start_urls = ['http://dmoztools.net/Computers/Programming/Languages/Python/Resources/','http://dmoztools.net/Computers/Programming/Languages/Python/Books/']


    def parse(self, response):
        for sel in response.xpath('//div[@class="title-and-desc"]'):
            item = ScrapyExampleItem()
            item['title'] = sel.xpath('./a/div/text()').extract()[0] # 标题
            item['link'] =  sel.xpath('./a/@href').extract()[0] # 链接
            item['desc'] =  sel.xpath('./div/text()').extract()[0].strip()
            yield item

