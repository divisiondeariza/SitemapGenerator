# -*- coding: utf-8 -*-
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from ScraperDANE.LinksFormatter import LinksFormatter
from ScraperDANE.items import ScraperdaneItem



class DaneSpider(CrawlSpider):
    formatter = LinksFormatter()
    name = "Dane"
    domain = "funes.uniandes.edu.co"
    allowed_domains = [domain]
    start_urls = (
        'http://' + domain,
    )

    rules = [Rule(LxmlLinkExtractor(allow=(), allow_domains = domain , process_value = formatter.formatLink), 'parsePages', follow =True)]

    def parsePages(self, response):
        linkExtractor = LxmlLinkExtractor(deny_extensions=[], process_value = self.formatter.formatLink)
        item = ScraperdaneItem()
        item["name"] = response.url
        item["children"] = [link.url for link in linkExtractor.extract_links(response)]
        return item
    