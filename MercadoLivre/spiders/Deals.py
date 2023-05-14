import scrapy


class DealsSpider(scrapy.Spider):
    name = 'Deals'

    def start_requests(self):
        yield scrapy.Request(url='https://lista.mercadolivre.com.br/ofertas', callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})

    def parse(self, response, **kwargs):
        for promotion in response.xpath('//li[@class="ui-search-layout__item shops__layout-item"]'):
            product_image = promotion.xpath('.//img/@data-src').get()
            product_title = promotion.xpath('.//h2/text()').get()
            product_price = promotion.xpath(
                './/span[@class="price-tag-fraction"]//text()').get()

            yield {
                'product_image': product_image,
                'product_title': product_title,
                'product_price': product_price,
            }
