'''
Created on 6/07/2015

@author: EJArizaR
'''

from scrapy.crawler import CrawlerProcess
from spiders.Dane import DaneSpider

class SpiderLauncher:
    def run(self, linksFilePath):
        settings = {"LOG_LEVEL": "WARNING",
                    "FEED_FORMAT": "json",
                    "FEED_URI": "file:///" + linksFilePath}
        process = CrawlerProcess(settings)
        spider = DaneSpider()        
        process.crawl(spider)
        process.start() 
