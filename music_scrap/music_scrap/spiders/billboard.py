# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider
from music_scrap.items import SingerItem


class ExampleSpider(CrawlSpider):
    name = "billboard"
    allowed_domains = ["billboard.com"]
    start_urls = (
        'http://www.billboard.com/artists/top-100',
    )
    rules = (
        Rule(SgmlLinkExtractor(allow=('/artists/?')), callback='parse_singer'),
    )

    def parse_singer(self, response):
        for item in response.xpath('//tr/td/div/span'):
            try:
                singer = SingerItem()
                singer['name'] = item.xpath('a/text()').extract()[0]
                singer['description'] = item.xpath('a/@href').extract()[0]
                singer.save()
            except:
                pass
