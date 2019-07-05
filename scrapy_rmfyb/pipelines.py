# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import pymongo

from scrapy_rmfyb import settings

class ScrapyQiubaiPipeline(object):
    def __init__(self):
        self.fp = None

    # 开始爬虫时,执行一次
    def open_spider(self,spider):
        self.fp = open('./data.txt','w',encoding="utf8")

    def process_item(self, item, spider):
        self.fp.write(item["author"]+":"+item["data"]+'\n')
        return item

    # 结束爬虫时,执行一次
    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束")

class ScrapyQiubaiPipeline_MongoDB(object):
    def __init__(self):
        self.table = settings.MONGODB_TABLENAME
        self.db = None
    # 开始爬虫时,执行一次
    def open_spider(self,spider):
        # 建立连接
        self.client = pymongo.MongoClient(host=settings.MONGODB_HOST,
                                      port = settings.MONGODB_PORT,
                                      username = settings.MONGODB_USER,
                                      password = settings.MONGODB_PASSWORD,
                                      )
        # 连接数据库
        self.db = self.client[settings.MONGODB_DBNAME]

    def process_item(self, item, spider):
        self.db[self.table].insert_one({"title":item["data"],"author":item["author"]})
        return item

    # 结束爬虫时,执行一次
    def close_spider(self,spider):
        self.client.close()
        print("爬虫结束")

class ScrapyRmfybPipeline(object):
    def __init__(self):
        if not os.path.exists('./data'):
            os.makedirs('./data')
        self.fp = None

    # 开始爬虫时,执行一次
    def open_spider(self,spider):
        pass

    def process_item(self, item, spider):
        date = item['date']
        title = item['title']
        directory_name = item['directory']
        data_list = item['data_list']
        path = 'data/'+date+'/'+directory_name
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path+'/'+title+'.txt','w',encoding='utf8') as f :
            f.write(title+"\n")
            for text in data_list:
                f.write(text+'\n')

        return item

    # 结束爬虫时,执行一次
    def close_spider(self,spider):
        print("爬虫结束")