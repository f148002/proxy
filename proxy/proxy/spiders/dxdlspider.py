# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem

class DxdlspiderSpider(scrapy.Spider):
    name = 'dxdlspider'
    allowed_domains = ['xicidaili.com']
    start_urls = []

    for i in range(1, 10):
        start_urls.append('https://www.xicidaili.com/wt/' + str(i))

    def parse(self, response):
        item = ProxyItem()
        # mian = response.xpath('//tr')

        # for li in mian:
        #     # 找到ip地址
        #     ip = li.xpath('/td').extract()[1]
        #     # 找到端口：
        #     port = li.xpath('/td/text()').extract()[2]
        #     # 将两者连接，并返回给item处理
        #     item['addr'] = ip + ':' + port
        #     yield item

        ip_list = response.xpath('//tr/td[2]/text()').extract()
        port_list = response.xpath('//tr/td[3]/text()').extract()

        temp = []
        for i in range(0, len(ip_list)):
            # temp.append(ip_list[i] + ':' + port_list[i])
            item['addr'] = ip_list[i] +':'+ port_list[i]
            yield item
