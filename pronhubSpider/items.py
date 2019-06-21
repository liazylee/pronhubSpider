# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class PronhubspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_title=Field()
    image_url=Field()
    video_duration=Field()
    quality_480p=Field()
    video_views=Field()
    video_rating=Field()
    link_url=Field()
    pass
