# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from imooc.items import ImoocItem
from scrapy.http import Request


class Imooc(CrawlSpider):
    name='imooc'
    allowed_domains = ['imooc.com']
    start_urls = []
    for pn in range(1,31):
        url = 'http://www.imooc.com/course/list?page=%s' % pn
        start_urls.append(url)

    def parse(self,response):
        item=ImoocItem()
        selector=Selector(response)
        # Course = selector.xpath('//a[@class="course-card"]')
        Course = selector.xpath('// a[@class="course-card"]')

        for eachCourse in Course:
            Course_name = eachCourse.xpath('div[@class="course-card-content"]/h3[@class="course-card-name"]/text()').extract()[0]

            Course_content = eachCourse.xpath('div[@class="course-card-content"]/div[@class="clearfix course-card-bottom"]/p[@class="course-card-desc"]/text()').extract()[0]

            Course_level = eachCourse.xpath('div[@class="course-card-content"]/div[@class="clearfix course-card-bottom"]/div[@class="course-card-info"]/span/text()').extract()[0]

            Course_attendance = eachCourse.xpath('div[@class="course-card-content"]/div[@class="clearfix course-card-bottom"]/div[@class="course-card-info"]/span/text()').extract()[1]

            # # Course_name = eachCourse.xpath('//  a / div[2] / h3[@class="course-card-name"]/text()').extract()[0]
            # Course_name = eachCourse.xpath('//  a / div[2] / h3[@class="course-card-name"]/text()').extract()[0]
            # # Course_content = eachCourse.xpath('// a / div[2] / div / p[@class="course-card-desc"]/text()').extract()
            # Course_content = eachCourse.xpath('div[@class="course-card-content"]/div[@class="clearfix course-card-bottom"]/p[@class="course-card-desc"]/text()').extract()[0]
            # # # Course_level = eachCourse.xpath('//a/div[2]/div/div/span[1]/text()').extract()[0]
            # Course_level = eachCourse.xpath('//a/div[2]/div/div/span[1]/text()').extract()[0]
            # # # Course_attendance = eachCourse.xpath('// a / div[2] / div / div / span[2] / text()').extract()[1]
            # Course_attendance = eachCourse.xpath('// a / div[2] / div / div / span[2] / text()').extract()[1]
            item['Course_name'] = Course_name
            # item['Course_content'] = ';'.join(Course_content)
            item['Course_content'] = Course_content
            item['Course_level'] = Course_level
            item['Course_attendance'] = Course_attendance
            yield item