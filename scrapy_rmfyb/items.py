# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyQiubai(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    data = scrapy.Field()
    # pass

class ScrapyRmfyb(scrapy.Item):
    date = scrapy.Field()   # 目录从属的 日期
    directory = scrapy.Field()  # 文件从属的目录名字
    title = scrapy.Field() # 文章标题
    data_list = scrapy.Field() # 文章列表, 每个字符串是一个段落
