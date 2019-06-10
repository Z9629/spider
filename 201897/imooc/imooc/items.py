# # -*- coding: utf-8 -*-
#
# # Define here the models for your scraped items
# #
# # See documentation in:
# # https://doc.scrapy.org/en/latest/topics/items.html
#
# import scrapy
#
#
# class ImoocItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

#######################
from  scrapy import Item,Field
class ImoocItem(Item):
    Course_name=Field()#课程名称
    Course_content=Field()#课程内容
    Course_level=Field()#课程等级
    Course_attendance=Field()#课程学习人数