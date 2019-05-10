# -*- coding: utf-8 -*-
import scrapy


class ProxiesSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['www.kuaidaili.com']
    base_url_1 = 'http://www.kuaidaili.com/free/inha/{}/'
    base_url_2 = 'https://www.kuaidaili.com/free/intr/{}/'
    start_urls = []
    for num in range(1, 10):
        start_urls.append(base_url_1.format(num))
        start_urls.append(base_url_2.format(num))

    def parse(self, response):

        ip = response.xpath('//td[@data-title="IP"]/text()').extract()
        port = response.xpath('//td[@data-title="PORT"]/text()').extract()

        for ip, port in zip(ip, port):
            item = {}
            http_proxie = '%s:%s' % (ip, port)
            item['代理地址'] = http_proxie
            # print(item)
            yield item
