# -*- coding: utf-8 -*-
import scrapy

from xunleidownload.items import XunleidownloadItem



class QiqipuSpider(scrapy.Spider):
    name = 'qiqipu'
    allowed_domains = ['gougou2018.com']
    # start_urls是我们准备爬的初始页面 例如和平饭店
    start_urls = ['http://www.gougou2018.com/oumei/20920/']

    def parse(self, response):
        movies = response.xpath('//div[@class="play-list"]/ul/li')
        for each_movie in movies:
            item = XunleidownloadItem()
            item['name'] = each_movie.xpath('./a/@href').extract()[0]
            yield item



