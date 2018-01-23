import scrapy

from scrapy.loader.processors import Join


class CourseItem(scrapy.Item):
    
    title = scrapy.Field()
    headline = scrapy.Field()
    url = scrapy.Field()
    instructors = scrapy.Field()
    lectures = scrapy.Field(
        output_processor=Join(' | ')
    )
    image = scrapy.Field()
