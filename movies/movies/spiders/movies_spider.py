from scrapy import Spider
from scrapy.http.request import Request
from movies.items import MoviesItem
import re


class MoviesSpider(Spider):

    name = "movies_spider"
    allowed_urls = ['https://web.archive.org/', 'https://www.imdb.com/']
    start_urls = ['https://web.archive.org/web/20200703054205if_/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20200717163605/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20200915062314if_/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20201001015001/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20201013174350if_/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20201116015019if_/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm']


    def parse(self, response):

        urls = ['https://web.archive.org/web/20200703054205if_/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20200717163605/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20200915062314if_/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20201001015001/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20201013174350if_/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://web.archive.org/web/20201116015019if_/https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm','https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm']

        rank_dates = ['2020-07-03', '2020-01-17','2020-09-15', '2020-10-01', '2020-10-13', '2020-11-16', '2021-02-11']

        urls_and_dates = list(zip(urls, rank_dates))
        
        for url, date in urls_and_dates:

            rank_date = date
            
            yield Request(url=url, callback=self.parse_movies_page, meta={'rank_date':rank_date})

    def parse_movies_page(self, response):


        rows = response.xpath('//tbody[@class="lister-list"]/tr')

        for i in range(0, len(rows)):
           
            try:
                rank = int(rows[i].xpath('.//div[@class="velocity"]/text()').get().strip())
            except:
                rank = int(re.findall(r'(\d+)[^\d]', rows[i].xpath('.//div[@class="velocity"]/text()').get())[0])
            
            movie_name = rows[i].xpath('.//td[2]/a/text()').get()

            

            item = MoviesItem()



            item['movie_name'] = movie_name
            item['rank'] = rank
            item['rank_date'] = response.meta['rank_date']

            yield item




