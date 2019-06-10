
import requests
from lxml import etree
import csv
import pandas as pd
import time
import random


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Referer':'http://www.huanyue123.com/book/'
}
# base_url = "https://www.baidu.com/"
base_url = "https://news.baidu.com/"
req = requests.get(base_url,headers=headers)

html_doc = req.content.decode("utf-8")
# print(html_doc)

# xpath解析


# 建立html的树
tree = etree.HTML(html_doc)
values = []
for i in range(10):
    items = tree.xpath('//div[@class="hotnews"]//a/text()')[i]
    items2 = tree.xpath('//div[@class="hotnews"]//a/@href')[i]
    list = [items, items2]
    values.append(list)
    # print(items,items2)

name = ['text','href']
test = pd.DataFrame(columns=name,data=values)
test.to_csv(r'C:\Users\14813\Desktop\新建文件夹\data.csv', encoding='utf_8_sig')
