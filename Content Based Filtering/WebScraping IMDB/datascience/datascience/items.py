# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DatascienceItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    imdb_score = scrapy.Field()
    runtime = scrapy.Field()
    genre = scrapy.Field()
    rating = scrapy.Field()
    cast_crew = scrapy.Field()
    votes = scrapy.Field()
    description = scrapy.Field()
    gross = scrapy.Field()
    pass
