# -*- coding: utf-8 -*-
import scrapy


class ProxiesSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['www.xicidaili.com']
    base_url = 'https://www.xicidaili.com/nn/{}'

    def start_requests(self):
        for num in range(1, 6):
            yield scrapy.Request(
                url=self.base_url.format(num)
            )

    def parse(self, response):
        ip= response.xpath('//tr/td[2]/text()').extract()
        port = response.xpath('//tr/td[3]/text()').extract()
        for ip, port in zip(ip, port):
            item = {}
            item['代理地址'] = '%s:%s' % (ip, port)
            print(item)
            yield item