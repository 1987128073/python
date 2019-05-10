# -*- coding: utf-8 -*-
import scrapy


class ProxiesSpider(scrapy.Spider):
    name = 'zdaye'
    allowed_domains = ['ip.zdaye.com']
    base_url = 'http://ip.zdaye.com/dayProxy/{}.html'
    cookie_string = "acw_tc=781bad2915574916824314920e08eb65a1db56e971639f768cff311012ded1; ASPSESSIONIDQCRBRCTA=AEKBLGLCLABLNGDBNKKIDAJG; __51cke__=; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1557491683,1557491984,1557491989; __tins__16949115=%7B%22sid%22%3A%201557493550968%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201557495742023%7D; __51laig__=18; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1557493942"

    cookies = dict([cookie_str.split('=') for cookie_str in cookie_string.split('; ')])

    def start_requests(self):
        for num in range(1, 5):
            yield scrapy.Request(
                url=self.base_url.format(num),
                cookies=self.cookies
            )

    def parse(self, response):
        all_list = response.xpath('//h3[@class="thread_title"]/a/@href').extract()
        for a in all_list:
            url = 'http://ip.zdaye.com' + a
            yield scrapy.Request(
                url=url,
                cookies=self.cookies,
                callback=self.parse_detail
            )

    def parse_detail(self, response):
        ip_port = response.xpath('//div[@class="cont"]/text()').extract()
        if ip_port is not None:
            for pro in ip_port:
                item = {}
                item['代理地址'] = pro.split('@')[0]
                print(item)
                yield item