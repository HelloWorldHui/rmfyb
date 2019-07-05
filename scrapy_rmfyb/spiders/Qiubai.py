# -*- coding: utf-8 -*-
import scrapy
from scrapy_rmfyb.items import ScrapyQiubai

class QiubaiSpider(scrapy.Spider):
    name = 'Qiubai'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']
    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(url=u,callback=self.parse)

    page_num = 1
    def parse(self, response):
        # tree = etree.HTML(response.text)
        # print(response.xpath('//*[@id="content"]/div/div[2]/div/ul/li')) # <Selector>
        # print(tree.xpath('//*[@id="content"]/div/div[2]/div/ul/li')) # <Element>
        # 爬取首页文章的标题和作者
        li_list = response.xpath('//*[@id="content"]/div/div[2]/div/ul/li')

        data_list = []
        for li in li_list:
            title = li.xpath('.//div/a/text()')[0].extract()
            author = li.xpath('.//div/div/a/span/text()')[0].extract()
            item = ScrapyQiubai()
            item["author"] = author
            item["data"] = title
            yield item
        if self.page_num <= 10:
            self.page_num += 1
            url = 'https://www.qiushibaike.com/8hr/page/%s/' %self.page_num
            print(url)
            yield scrapy.Request(url=url,callback=self.parse)

        #     dic = {"title":title,"author":author}
        #     data_list.append(dic)
        # return data_list