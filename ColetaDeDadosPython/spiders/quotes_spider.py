import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    i = 1

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1'
        ]
        

    def parse(self, response):
        
        for author in response.xpath('.//life//').getall():
            if author.xpath('.//small[@class="author"]//text()') == 'Mark Twain':
                filename = f'quotes-{i}.txt'
                i += 1
                with open(filename, 'wb') as f: 
                    f.write(response.css("life.author::text").get())
                    self.log(f'Saved file {filename}')

        for tag in response.xpath('.//span[@class="text"]//text()').getall():
            if tag.xpath('.//span[@class="text"]//text()').get() == 'truth':
                filename = f'quotes-{i}.txt'
                i += 1
                with open(filename, 'wb') as f:
                    f.write(tag.xpath('.//span[@class="text"]//text()').get())
                    self.log(f'Saved file {filename}')
        
        next_page = response.xpath('//a[contains(@title, "Next")]/@href').get()
        if next_page:
            yield scrapy.Request(url = next_page, callback=self.parse)