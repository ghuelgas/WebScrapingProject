# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HispodcastItem(scrapy.Item):
    

    name = scrapy.Field()
    creator = scrapy.Field()
    rank = scrapy.Field()
    rank_date = scrapy.Field()

