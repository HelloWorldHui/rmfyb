import requests
from lxml import etree
from datetime import datetime
if __name__ == "__main__":

    url = 'http://sc.chinaz.com/tupian/gudianmeinvtupian.html'
    headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    #获取页面文本数据
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    #解析页面数据（获取页面中的图片链接）
    #创建etree对象
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@id="container"]/div')
    #解析获取图片地址和图片的名称
    for div in div_list:
        image_url = div.xpath('.//img/@src2')
        image_name = div.xpath('.//img/@alt')
        print(image_url) #打印图片链接
        print(image_name)#打印图片名称
