# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import AnimationItem


class YunbtvSpider(CrawlSpider):
    name = 'fengchedm'
    allowed_domains = ['www.fengchedm.com']
    start_urls = ['http://www.fengchedm.com/list/138-1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/list/138-'), follow=True),
        Rule(LinkExtractor(allow=r'/content/'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):
        # url = self.url.append(response.url)

        item = AnimationItem()
        item['name'] = response.xpath('//span[@class="names"]/text()').extract_first()
        item['picture_url'] = response.xpath("//img[@class='lazy']/@src").extract_first()
        a = response.xpath('//div[@class="clearfix"][1]/ul/li').extract()

        item['count'] = len(a)
        item['spider_name'] = self.name

        yield item

