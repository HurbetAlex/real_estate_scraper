import scrapy
from real_estate_scraper.items import RealEstateScraperItem

class RealEstateSpider(scrapy.Spider):
    name = 'real_estate'
    start_urls = [
        'https://kelm-immobilien.de/immobilien',
        'https://www.adentz.de/wohnung-mieten-rostock/#/list1',
        'https://bostad.herbo.se'
    ]


    def parse(self, response):
        if 'kelm-immobilien' in response.url:
            yield from self.parse_kelm(response)
        elif 'adentz' in response.url:
            yield from self.parse_adentz(response)
        elif 'bostad.herbo' in response.url:
            yield from self.parse_bostad(response)

    def parse_kelm(self, response):
        for property in response.css('div.property-listing'):
            item = RealEstateScraperItem()
            item['url'] = response.urljoin(property.css('a::attr(href)').get())
            item['title'] = property.css('h2.property-title::text').get()
            item['status'] = property.css('span.status::text').get()
            item['pictures'] = property.css('div.pictures img::attr(src)').getall()
            item['rent_price'] = property.css('span.price::text').re_first(r'\d+,\d+').replace(',', '.')
            item['description'] = property.css('div.description::text').get()
            item['phone_number'] = property.css('span.phone::text').get()
            item['email'] = property.css('span.email::text').get()
            yield item


    def parse_adentz(self, response):
        for property in response.css('div.property-listing'):
            item = RealEstateScraperItem()
            item['url'] = response.urljoin(property.css('a::attr(href)').get())
            item['title'] = property.css('h2.property-title::text').get()
            item['status'] = property.css('span.status::text').get()
            item['pictures'] = property.css('div.pictures img::attr(src)').getall()
            item['rent_price'] = property.css('span.price::text').re_first(r'\d+,\d+').replace(',', '.')
            item['description'] = property.css('div.description::text').get()
            item['phone_number'] = property.css('span.phone::text').get()
            item['email'] = property.css('span.email::text').get()
            yield item

    def parse_bostad(self, response):
        for property in response.css('div.property-listing'):
            item = RealEstateScraperItem()
            item['url'] = response.urljoin(property.css('a::attr(href)').get())
            item['title'] = property.css('h2.property-title::text').get()
            item['status'] = property.css('span.status::text').get()
            item['pictures'] = property.css('div.pictures img::attr(src)').getall()
            item['rent_price'] = property.css('span.price::text').re_first(r'\d+,\d+').replace(',', '.')
            item['description'] = property.css('div.description::text').get()
            item['phone_number'] = property.css('span.phone::text').get()
            item['email'] = property.css('span.email::text').get()
            yield item
