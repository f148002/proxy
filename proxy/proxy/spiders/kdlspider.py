# -*- coding: utf-8 -*-
import scrapy


class KdlspiderSpider(scrapy.Spider):
    name = 'kdlspider'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://kuaidaili.com/']

    def parse(self, response):
        pass
