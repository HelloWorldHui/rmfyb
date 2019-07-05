# coding=utf
"""
author=Hui_T
"""
import requests
from lxml import etree

response = requests.get('https://www.1919.cn/search.html?stype=p&kw=%E9%85%92')
tree = etree.HTML(response.text)

a = tree.xpath('/html/body/div[5]/div/div[3]/div[2]/div[3]/ul/span/span/li[9]/a/text()')
print(a)