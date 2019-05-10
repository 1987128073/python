# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ProxiePoolPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json

from pymongo import MongoClient


class JsonPipeline(object):

    def open_spider(self, spoder):
        self.f = open('new_proxies.json', 'w', encoding='utf-8')
        self.f.write('[')

    def close_spider(self, spider):
        self.f.write(']')
        self.f.close()

    def process_item(self, item, spider):
        json.dump(item, self.f, ensure_ascii=False, indent=2)
        self.f.write(',')
        return item

class MongoDBPipeline(object):
    def open_spider(self,spider):
        client = MongoClient(host='127.0.0.1', port=27017)
        self.db = client.proxies

    def close_spider(self,spider):
        pass

    def process_item(self,item,spider):
        self.db.items.insert(item)
        return item