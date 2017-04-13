# -*- coding: utf-8 -*-
import scrapy
from scrapy_doubantop250.items import  ScrapyDoubantop250Item

class DoubanmSpider(scrapy.Spider):
    name = "doubanm"
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        sels = response.xpath('//*[@id="content"]/div/div[1]//li')
        for sel in sels:
            item = ScrapyDoubantop250Item()
            item['name'] = sel.xpath('.//span/text()').extract()[0]
            item['rank'] = sel.xpath('.//*[@class="rating_num"]/text()').extract()[0]
            yield item

        try:
            next_page= response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()[0]
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        except:
            pass

