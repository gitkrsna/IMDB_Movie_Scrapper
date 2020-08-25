import scrapy
from crawling.items import MovieItem
from scrapy.spiders import CrawlSpider


class RottenTomatoesSpider(CrawlSpider):
    name = 'rottentomatoes'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top',]

    def parse(self, response):
        rows = response.xpath('//*[@class="lister-list"]/tr/td[2]/a/@href').extract()
        for row in rows:
            link = 'http://www.imdb.com' + row
            yield scrapy.Request(url=link, callback=self.parse_item)


    def parse_item(self, response):
        item = MovieItem()
        item['title'] = response.xpath('//div[@class="title_wrapper"]/h1/text()').extract_first()
        item['year'] = response.xpath('//div[@class="title_wrapper"]/h1/span/a/text()').extract_first()
        item['rating'] = response.xpath('//span[@itemprop="ratingValue"]/text()').extract_first()
        item['duration'] = response.xpath('//div[@class="subtext"]/time/text()').extract_first()
        item['genres'] = response.xpath('//div[@class="see-more inline canwrap"]/a/text()').extract()
        item['director'] = response.xpath('//div[@class="credit_summary_item"]/a/text()').extract_first()
        return item
