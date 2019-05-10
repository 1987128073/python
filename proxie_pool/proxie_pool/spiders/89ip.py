# -*- coding: utf-8 -*-
import scrapy


class ProxiesSpider(scrapy.Spider):
    name = '89ip'
    allowed_domains = ['www.89ip.cn']
    base_url = 'http://www.89ip.cn/index_{}.html'
    start_urls = []
    for num in range(1, 15):
        start_urls.append(base_url.format(num))

    def parse(self, response):
        ip = response.xpath('//table[@class="layui-table"]/tbody/tr/td[1]/text()').extract()
        port = response.xpath('//table[@class="layui-table"]/tbody/tr/td[2]/text()').extract()

        for ip, port in zip(ip, port):
            item = {}
            ip = ip.replace('\n\t\t\t', '').replace('\t\t', '')
            port = port.replace('\n\t\t\t', '').replace('\t\t', '')
            http_proxie = '%s:%s' % (ip, port)
            # https_proxie = 'https://%s:%s' % (ip, port)
            item['代理地址'] = http_proxie
            yield item
