import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        return {
            # title = response.css('span.title:text').get()
            'number': response.xpath('//span[@class="rfc-no"]/text()').get(),
            'title': response.xpath('//span[@class="title"]/text()').get(),
            'description': response.xpath('//meta[@name="DC.Desription.Abstract"]/@content').get(),
            'date': response.xpath('//pre/span[@class="date"]/text()').get(),
            'subtitles': response.xpath('//div/span[@class="subtitles"]/text()').get(),
            'text': w3lib.html.remove_tags(response.xpath('//div/span/text()').get()),
            'working-group': response.xpath('//div/span[@class="subheading"]/text()').get(),
            'request-for-comments': response.xpath('//div/span[@class="subtitles"]/text()').get(),
            'author': response.xpath('//pre/span[@class="author-name"]/text()').get(),
            'author-company': response.xpath('//pre/span[@class="author-company"]/text()').get(),
            'author-address': response.xpath('//span[@class="address"]/text()').get(),
            'phone': response.xpath('//span[@class="phone"]/text()').get(),
            'email': response.xpath('//span[@class="email"]/text()').get(),
            'source': response.xpath('//head[@profile]')
        }
    