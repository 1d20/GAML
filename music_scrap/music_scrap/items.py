# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# cd music_scrap/music_scrap/
# scrapy crawl billboard

import sys
sys.path.append('/Users/detonavomek/Documents/Django/gaml')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'source.settings'

import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from apps.core.models import Singer


class SingerItem(DjangoItem):
    django_model = Singer
# class SingerItem(scrapy.Item):
#     name = scrapy.Field()
#     description = scrapy.Field()
