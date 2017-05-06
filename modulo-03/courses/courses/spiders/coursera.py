import scrapy


class CourseraSpider(scrapy.Spider):

    name = "coursera"
    start_urls = ['https://www.coursera.org/browse?languages=pt']

    def parse(self, response):
        categories = response.xpath("//div[contains(@class, 'rc-DomainNav')]/a")
        for cat in categories:
            cat_url = cat.xpath('./@href').extract_first()
            self.log('Category: %s' % cat_url)
            yield scrapy.Request(
                url='https://www.coursera.org%s' % cat_url,
                callback=self.parse_category
            )
    
    def parse_category(self, response):
        self.log(response.xpath("//title/text()").extract_first())
