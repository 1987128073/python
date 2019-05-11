# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import AnimationItem


class YunbtvSpider(CrawlSpider):
    name = 'yunbtv'
    allowed_domains = ['www.yunbtv.com']
    start_urls = ['https://www.yunbtv.com/vodtype/dongman.html']

    rules = (
        Rule(LinkExtractor(allow=r'/vodtype/dongman', deny=r'/vodtype/dongman-1.html'), follow=True),
        Rule(LinkExtractor(allow=r'/voddetail/'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):
        # url = self.url.append(response.url)

        item = AnimationItem()
        item['name'] = response.xpath('//h2[@class="hidden-xs"]/a/text()').extract_first()
        item['picture_url'] = response.xpath('//div[@class="row"]/div[1]/img/@src').extract_first()
        a = response.xpath('//ul[@class="clearfix"]/li').extract()

        item['count'] = len(a)
        item['spider_name'] = self.name
        yield item

