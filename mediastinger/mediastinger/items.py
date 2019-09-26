# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MediastingerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
	intheaters = scrapy.Field()
    onvideo = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    genre = scrapy.Field()
    productionco = scrapy.Field()
    distributor = scrapy.Field()
    mpaa = scrapy.Field()
    website = scrapy.Field()
    ourreview = scrapy.Field()
    runningtime = scrapy.Field()
    creditstime = scrapy.Field()
    during = scrapy.Field()
    after = scrapy.Field()
    url = scrapy.Field()
