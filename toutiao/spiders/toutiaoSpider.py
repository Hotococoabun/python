# -*- coding: utf-8 -*-
import scrapy


class ToutiaospiderSpider(scrapy.Spider):
    name = 'toutiaoSpider'
    allowed_domains = ['toutiao.com']
    start_urls = ['http://toutiao.com/']

    def start_requests(self):
        url = 'http://www.toutiao.com/api/pc/feed/?category=military_world&utm_source=toutiao&widen='
        for x in range(1,21):
            yield scrapy.Request(url+str(x), callback=self.parse)

    def parse(self, response):
        text = response.text.replace('true','True').replace('false','False')
        data = eval(text)['data']
    #    print (len(data))
        for x in data:
            # print(x)
            # print(type(x))
            print ('    url -> ', 'http://www.toutiao.com'+ x['source_url'])
            print (' title  -> ', x['title'])
            print ('abstract-> ', x['abstract'])

            print ("\n")
