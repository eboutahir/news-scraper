# -*- coding: utf-8 -*-
import scrapy

num_pages = 5
class NewsspiderSpider(scrapy.Spider):
    name = 'newsSpider'
    start_urls = ['https://time.com/section/tech/?page={}'.format(i+1) for i in range(num_pages)]

    def parse(self, response):
        data={}
        news = response.css('section.content')
        for item in news:
            for element in item.css('article.partial'):
                for e in element.css('h3.headline'):
                    data['ArticleTitle'] = e.xpath('normalize-space(.//a)')[0].extract()
                data['ArticleUrl'] = element.css('h3.headline a::attr(href)').getall()
                for e in data['ArticleUrl']:
                    data['ArticleUrl'] = 'https://time.com' + e
                data['ArticleSummary'] = element.css('div.article-info-extended div.summary.margin-8-bottom.desktop-only::text').getall()[0].strip()
                yield data