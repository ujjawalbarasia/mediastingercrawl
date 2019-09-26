# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from mediastinger.items import MediastingerItem

class Mediastinger1Spider(CrawlSpider):
    name = 'mediastinger1'
    allowed_domains = ['www.mediastinger.com']
    start_urls = ['http://www.mediastinger.com/in-theaters/']
    rules= (
		Rule(LinkExtractor(allow=(), restrict_css=('.thumbnail',)),
             callback="parse_item",
             follow=False),)
def parse_item(self, response):
        item_links = response.css('.divwidth > .title::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
        extras = response.css('.pricelabel > strong::text').extract()[0]
        intheaters =
        onvideo =
        director =
        actor =
        genre =
        productionco =
        distributor =
        mpaa =
        website =
        ourreview =
        runningtime =
        creditstime =
        during =
        after =
        item = MediastingerItem()
        item['title'] = title
        item['extras'] = extras
        item['intheaters'] = intheaters
        item['onvideo'] = onvideo
        item['director'] = director
        item['actor'] = actor
        item['genre'] = genre
        item['productionco'] = productionco
        item['distributor'] = distributor
        item['mpaa'] = mpaa
        item['website'] = website
        item['ourreview'] = ourreview
        item['runningtime'] = runningtime
        item['creditstime'] = creditstime
        item['during'] = during
        item['after'] = after
        item['url'] = response.url
        yield item

   


    
