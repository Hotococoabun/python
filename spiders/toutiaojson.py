# -*- coding: utf-8 -*-
import scrapy


class ToutiaojsonSpider(scrapy.Spider):
    name = 'toutiaojson'
    allowed_domains = ['toutiao.com']
    start_urls = ['http://toutiao.com/']

    def start_requests(self):
        pass

    def parse(self, response):
        pass
