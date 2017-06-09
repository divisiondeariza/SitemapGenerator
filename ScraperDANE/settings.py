# -*- coding: utf-8 -*-


# Scrapy settings for ScraperDANE project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ScraperDANE'
LOG_LEVEL = "INFO"
SPIDER_MODULES = ['ScraperDANE.spiders']
NEWSPIDER_MODULE = 'ScraperDANE.spiders'
FEED_URI = "file:///C:/Users/ejarizar/workspace/SitemapGenerator/equis.json"
FEED_FORMAT = "json"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScraperDANE (+http://www.yourdomain.com)'
