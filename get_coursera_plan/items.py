# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetCourseraPlanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    week = scrapy.Field()
    deadline = scrapy.Field()
    lesson_name = scrapy.Field()
    tip_name = scrapy.Field()
    tip_duration=scrapy.Field()
    pass
