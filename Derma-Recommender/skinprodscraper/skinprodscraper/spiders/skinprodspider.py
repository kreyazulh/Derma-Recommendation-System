import scrapy
import re


class SkinprodspiderSpider(scrapy.Spider):
    name = "skinprodspider"
    allowed_domains = ["skinsort.com"]
    start_urls = ["https://skinsort.com/products/"]

    def parse(self, response):
        products  = response.css('div.w-full.h-full.flex.flex-wrap.justify-start.relative.min-w-full.break-words.px-2')


        for product in products:
            relative_url = product.css('span a ::attr(href)').getall()[1]
            product_url = 'https://skinsort.com'+relative_url
            yield response.follow(product_url, callback=self.product_parse)


        for i in range(2, 637, 1):  #2,637,1
            next_page_url = 'https://skinsort.com/products//page/'+str(i)
            yield response.follow(next_page_url, callback=self.parse)

    def product_parse(selfself, response):
        yield {
            'brand': response.css('h1 span a::text').get(),
            'name': response.css('div.w-full.max-w-7xl.flex.justify-center.flex-col.relative.mx-auto.px-3 div a ::text').getall()[2],
            'type': response.css('span.text-base.font-bold.text-left.font-body.bg-indigo-50.text-indigo-800.px-2.rounded-lg.leading-tight.py-1.mr-3.mt-1 a::text').get(),
            'country':response.css('span.flex.items-center.text-base.font-bold.text-left.font-body.bg-indigo-50.text-indigo-800.px-2.rounded-lg.leading-tight.py-1.mr-3.mt-1 img::attr(alt)').get(),
            'ingridients':  response.css('div.mt-4.flex.flex-col.text-left.text-base.text-blue-gray-800.mb-5.max-w-2xl p a::text').getall(),
            'features': [x for x in ' '.join( response.css('div.flex.flex-col.items-start.w-full.mb-10.text-sm div div div div.flex.flex-wrap.justify-center.pt-1::text').getall()).split('\n') if x != '' and x != ' '],
            'afterUse': [x for x in ' '.join( response.css('div.flex.flex-wrap.mt-2.mb-2 div div span::text').getall()).split('\n') if x != '' and x != ' ' and not x.startswith("(")]






        }

