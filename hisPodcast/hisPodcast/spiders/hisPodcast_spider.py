from scrapy import Spider
from scrapy.http.request import Request
from hisPodcast.items import HispodcastItem


class HispodcastSpider(Spider):

    name = "hisPodcast_spider"
    allowed_urls = ['https://web.archive.org/', 'https://chartable.com/']
    start_urls = ['https://web.archive.org/web/20200703023233/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach', 'https://web.archive.org/web/20200717181104/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach', 'https://web.archive.org/web/20200915233129/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach','https://web.archive.org/web/20201001082230/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach','https://web.archive.org/web/20201013140535/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach','https://web.archive.org/web/20201116033959/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach','https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach']


    def parse(self, response):

        urls = ['https://web.archive.org/web/20200703023233/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach', 'https://web.archive.org/web/20200717181104/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach', 'https://web.archive.org/web/20200915233129/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach','https://web.archive.org/web/20201001082230/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach','https://web.archive.org/web/20201013140535/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach','https://web.archive.org/web/20201116033959/https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach','https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach']

        for url in urls:
            yield Request(url=url, callback=self.parse_hisPodcast_page)

    def parse_hisPodcast_page(self, response):

        rank_date = response.xpath('//div[@class="fr"]/text()').get().strip()

        rows = response.xpath('//tr[@class="striped--near-white"]')

        for i in range(0, len(rows)):
           
            rank = rows[i].xpath('./td/div[@class="b header-font f2 tc"]/text()').get()

            name = rows[i].xpath('./td[3]//a[@class="link blue"]/text()').get()

            try:
                creator = rows[i].xpath('./td/a/text()').get()
            except:
                creator = rows[i].xpath('./td/div[@class="silver mb1 db"]/text()').get()

        

            item = HispodcastItem()



            item['name'] = name
            item['rank'] = rank
            item['creator'] = creator
            item['rank_date'] = rank_date

            yield item




