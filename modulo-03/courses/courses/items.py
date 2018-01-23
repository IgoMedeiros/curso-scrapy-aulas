import scrapy


class CourseItem(scrapy.Item):
    
    title = scrapy.Field()
    headline = scrapy.Field()
    url = scrapy.Field()
    instructors = scrapy.Field()
    lectures = scrapy.Field()
    image = scrapy.Field()
