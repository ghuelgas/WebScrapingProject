# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PodcastItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    creator = scrapy.Field()
    rating = scrapy.Field()
    num_ratings = scrapy.Field()
