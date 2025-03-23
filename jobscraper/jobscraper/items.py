# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscraperItem(scrapy.Item):
    job_position = scrapy.Field()
    salary = scrapy.Field()
    company = scrapy.Field()
