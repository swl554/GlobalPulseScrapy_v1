# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class jsonitem(scrapy.Item):
    file_link = scrapy.Field()
    json_file = scrapy.Field()

class csvitem(scrapy.Item):
    file_link = scrapy.Field()
    csv_file = scrapy.Field()

class txtitem(scrapy.Item):
    file_link = scrapy.Field()
    txt_file = scrapy.Field()

class datitem(scrapy.Item):
    file_link = scrapy.Field()
    dat_file = scrapy.Field()

class xlsitem(scrapy.Item):
    file_link = scrapy.Field()
    xls_file = scrapy.Field()

class linkitem(scrapy.Item):
    parent_link = scrapy.Field()
    link_url = scrapy.Field()
