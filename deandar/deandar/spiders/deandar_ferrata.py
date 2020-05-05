import re
import scrapy


class DeandarSpiter(scrapy.Spider):
    name = 'deandar'
    start_urls = ['https://deandar.com/en/ferratas/zona/Catalunya/']

    def parse(self, response):
        vf_links = response.css('.nruta a::attr(href)').getall()

        for vf_link in vf_links:
            if is_vf_detail_url(vf_link):
                yield response.follow(vf_link, self.parse_vf_detail)

    def parse_vf_detail(self, response):
        yield {
            'name': response.css('div#content_principal h1::text').get(),
            'rating': response.css('.votos_result .gran_numero::text').get(),
            'votes': response.css('.votos_result .nota_totales::text').get(),
            'grade': response.css('.inner_caract .dificultad::text').get().strip(),
            'status': response.css('#estat .fa-calendar *::text').get().strip(),
        }


vf_detail_page_pattern = re.compile("ferratas/[^/]+$")


def is_vf_detail_url(url):
    return vf_detail_page_pattern.search(url)
