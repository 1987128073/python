# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimationItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    picture_url = scrapy.Field()
    count = scrapy.Field()
    spider_name = scrapy.Field()
    # play_addr = scrapy.Field()

    pass
