# -*- coding: utf-8 -*-
import scrapy


class JdongSpider(scrapy.Spider):
    name = 'Jdong'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        print(response.text)
