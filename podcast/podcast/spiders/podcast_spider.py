from scrapy import Spider
from scrapy.http.request import Request
from podcast.items import PodcastItem
import re


class PodcastSpider(Spider):

    name = "podcast_spider"
    allowed_urls = ['https://chartable.com/']
    start_urls = ['https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach']

    def parse(self, response):

        rows = response.xpath('//tr[@class="striped--near-white"]')    
    

        url_list = rows.xpath('./td[3]//a[@class="link blue"]/@href').getall()

        for url in url_list:
            yield Request(url=url, callback=self.parse_podcast_page)

    def parse_podcast_page(self, response):

        name = response.xpath('//div/div[@class="f1-ns f2 fw1 mb2 dark-blue"]/text()').get()

        creator = response.xpath('//div/a[@class="link no-underline silver"]/text()').get()

        response.xpath('//div[@class="mt4"]/div[3]/text()').get()
        
        try:
            rating = float((response.xpath('//div[@class="mt4"]/div[3]/text()').get())[0:3])
        except:
            rating = None


        num_ratings_list = (re.findall(r'\d*,\d*', (response.xpath('//div[@class="mt4"]/div[3]/text()').get())[5:]))

        try:
            num_ratings = int(num_ratings_list[0].replace(",",""))
        except:
            num_ratings = None


        item = PodcastItem()



        item['name'] = name
        item['creator'] = creator
        item['rating'] = rating
        item['num_ratings'] = num_ratings
        

        yield item




