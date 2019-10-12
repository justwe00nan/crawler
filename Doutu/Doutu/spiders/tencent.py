# -*- coding:utf-8 -*-
import scrapy
from Doutu.items import DoutuItem

class TencentSpider(scrapy.Spider):
    name = 'tencent_spider'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']
    base_url='https://hr.tencent.com/position.php?&start='
    offset=0

    def parse(self, response):
        print(response)
        # node_list = response.xpath("//tr[@class='even'] or //tr[@class='odd']")
        #
        # for node in node_list:
        #     item = DoutuItem()
        #     #XPATH返回Xpath对象的列表，需要用extract()变成字符串列表,再取列表第一个元素
        #     item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0].encode('utf-8')
        #     item['positionLinks'] = node.xpath("./td[1]/a/@href").extract()[0].encode('utf-8')
        #     item['positionType'] = node.xpath("./td[2]/text()").extract()[0].encode('utf-8')
        #     item['positionNumber'] = node.xpath("./td[3]/text()").extract()[0].encode('utf-8')
        #     item['positionLocation'] = node.xpath("./td[4]/text()").extract()[0].encode('utf-8')
        #     item['positionTime'] = node.xpath("./td[4]/text()").extract()[0].encode('utf-8')
        #     print(item)
        #     yield item
        #
        # if self.offset<3351:
        #     self.offset+=10
        #     url=self.base_url+str(self.offset)
        #     #再次发送请求
        #     yield scrapy.Request(url,callback=self.parse)
