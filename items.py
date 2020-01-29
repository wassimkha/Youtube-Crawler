# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoutubecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    Subscriber = scrapy.Field()
    views = scrapy.Field()
    videos = scrapy.Field()
    link = scrapy.Field()
