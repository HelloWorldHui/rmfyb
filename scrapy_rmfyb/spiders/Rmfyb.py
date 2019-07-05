# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy_rmfyb.items import ScrapyRmfyb


class RmfybSpider(scrapy.Spider):
    name = 'Rmfyb'
    allowed_domains = ['rmfyb.chinacourt.org']
    start_urls = ['http://rmfyb.chinacourt.org/paper/html/2019-07/02/node_2.htm']
    date = '2010-01/01'
    url = 'http://rmfyb.chinacourt.org/paper/html/%s/%s'

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(url=u, callback=self.parse)

    def parse(self, response):
        directory_a_list = response.xpath('//*[@id="pageLink"]/@href').extract()  # 目录的超链接
        if directory_a_list:
            directory_a_list[0] = 'node_2.htm'
            for i in range(len(directory_a_list)):
                directory_a = directory_a_list[i]  # node_2.htm
                directory_name = directory_a.split('.')[0]  # node_2
                url = self.url % (self.date, directory_a)
                yield scrapy.Request(url=url, callback=self.parse_detail_a,
                                     meta={'directory_name': directory_name},dont_filter=True)

    def parse_detail_a(self, response):
        directory_name = response.meta['directory_name']  # 用于创建目录文件
        print(directory_name)
        # 详情页的超链接
        detail_a_list = response.xpath(
            '/html/body/table[1]/tr/td/table/tr/td[2]/table[2]/tr/td[1]/div/table/tr[2]/td/div/table/tbody/tr/td[2]/a'
        )
        if detail_a_list:
            for a in detail_a_list:
                a_href = a.xpath('.//@href').extract_first()
                detail_url = self.url % (self.date, a_href)
                yield scrapy.Request(url=detail_url, callback=self.parse_detail,
                                     meta={'directory_name': directory_name})

    def parse_detail(self, response):
        item = ScrapyRmfyb()
        item['directory'] = response.meta['directory_name']
        # 文章解析
        date = response.xpath(
            "/html/body/table[1]/tr/td/table/tr/td[2]/table[1]/tr/td[1]/font/strong/text()").extract_first()
        text_list = response.xpath('//*[@id="ozoom"]/p/text()').getall()
        title = response.xpath(
            "/html/body/table[1]/tr/td/table/tr/td[2]/table[2]/tr/td/table/tr[2]/td/div/table/tr[1]/td/table/tbody/tr[2]/td/text()").extract_first()
        date = date.strip().replace("/", "-")
        item['title'] = title
        item['date'] = date
        item["data_list"] = text_list
        yield item

        start_time = datetime.datetime.strptime(self.date,'%Y-%m/%d')
        end_time = datetime.datetime.now()
        one_day = datetime.timedelta(days=1)

        if start_time<= end_time:
            start_time += one_day
            self.date = start_time.strftime('%Y-%m/%d')
            yield scrapy.Request(url=self.url %(self.date,'node_2.htm'),callback=self.parse,dont_filter=True)
