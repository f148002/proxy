# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'dxdlspider':
            content = item['addr']
            with open(r'C:\Users\f1480\Desktop\Proxylist\dx_proxy.txt', 'a') as f:
                f.write(content + '\n')

        return item
