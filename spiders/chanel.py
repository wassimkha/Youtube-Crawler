# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import YoutubecrawlerItem

class ChanelSpider(scrapy.Spider):
    name = 'chanel'

    start_urls = ['https://www.channelcrawler.com/eng/results/49790']

    def parse(self, response):
        items = YoutubecrawlerItem()
        chanels = response.css(".col-lg-3")

        for chanel in chanels:
            title = chanel.css("h4 a::text").extract()
            all_info = chanel.css("a+ p small::text").extract()
            all_info = ' '.join([str(elem) for elem in all_info])

            all_info = re.sub('\s+', '', all_info)
            link = chanel.css("h4 a::attr(href)").extract()
            subscribers = float(all_info[0:all_info.find("S")-1])*1000
            videos = all_info[all_info.find("S")+11:all_info.find("V")]
            views = int(all_info[all_info.find("V")+6:all_info.find("T")].replace(",",""))


            items["link"] = link[0]
            items["Title"] = title[0]
            items["Subscriber"] = subscribers
            items["videos"] = videos
            items["views"] = views

            yield items

        next_page = response.css(".next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
