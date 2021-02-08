import scrapy, re

class ClutchSpider(scrapy.Spider):

    name = 'clutch'
    start_urls = ['https://clutch.co/it-services/outsourcing']

    def parse(self, response):

        # header for 
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

        items = response.xpath('//ul[re:test(@class, "directory-list")]//li/a[re:test(@href, "profile")]/@href').getall()
        for item in items:
            url = response.urljoin(item)
            yield scrapy.Request(url, callback=self.parse_company, headers=headers)

        # pages
        pg_next = response.css('.next a::attr(href)').get()
        if pg_next:
            pg_next_url = response.urljoin(pg_next)
            yield scrapy.Request(pg_next_url, callback=self.parse)

    def parse_company(self, response):

        # company
        company = response.css('.page-title::text').get()
        if company:
            company = re.sub(r'[^a-zA-Z0-9]+', ' ', company).strip()

        # score
        score = response.css('.rating::text').get()

        # presentation text
        text = response.xpath('//div//div[re:test(@class, "expanding-formatter-summary")]/p/text()').get()

        # services
        k_client = response.xpath('//article[re:test(@id, "portfolio")]//div[re:test(@class, "field-item even")]/text()').get()
        if k_client:
            k_client = k_client.strip()

        yield {
            'company': company,
            'score': score,
            'text': text,
            'clients': k_client
        }

