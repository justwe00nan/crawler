# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoutuItem(scrapy.Item):
    #职位名称
    positionName=scrapy.Field()
    #职位链接
    positionLinks=scrapy.Field()
    #职位类型
    positionType = scrapy.Field()
    #职位需求数量
    positionNumber = scrapy.Field()
    #职位地点
    positionLocation = scrapy.Field()
    #工作时间
    positionTime=scrapy.Field()


