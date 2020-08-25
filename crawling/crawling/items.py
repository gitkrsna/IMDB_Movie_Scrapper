# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html




import scrapy
from movie.models import Movie
from scrapy_djangoitem import DjangoItem
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 RuxitSynthetic/1.0 v6121910160 t38550 ath9b965f92 altpub"


class MovieItem(DjangoItem):
    django_model = Movie
    
