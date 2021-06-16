import scrapy
from lab1.items import ProductItem


class MebliumSpider(scrapy.Spider):
    name = "meblium"
    custom_settings = {
        'ITEM_PIPELINES': {
            'lab1.pipelines.MebliumPipeline': 300,
        },
        'CLOSESPIDER_PAGECOUNT': 3,
        'DEPTH_LIMIT': 0,
        'CLOSESPIDER_ITEMCOUNT': 20
    }
    fields = {
        'product': '//div[@class="product-container"]',
        'img': './div[@class="left-block"]/div[@class="product-image-container"]/a/img/@src',
        'name': './div[@class="right-block"]/h5/a/text()',
        'link': './div[@class="right-block"]/h5/a/@href',
        'price': './div[@class="right-block"]/div[@class="content_price"]/span/text()',
    }

    start_urls = ['https://meblium.com.ua/myagkaya-mebel/divany']
    allowed_domains = ['meblium.com.ua']

    def parse(self, response):
        for product in response.xpath(self.fields["product"]):
            prod = ProductItem()
            prod['productImage'] = product.xpath(self.fields['img-responsive']).extract()
            prod['productPrice'] = product.xpath(self.fields['price']).extract()
            prod['productName'] = product.xpath(self.fields['product-name']).extract()
            yield prod