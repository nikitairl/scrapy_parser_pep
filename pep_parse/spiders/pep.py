import scrapy
from pep_parse.items import PepParseItem
import re


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        peps = response.css("section#numerical-index").css("tbody").css("tr")
        for pep in peps:
            href = pep.css("a::attr(href)").get()
            if href is not None:
                yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css("h1.page-title::text").get()
        number = re.search(r"(?<=PEP )\d+", name)
        status = response.css("abbr::text").get()
        data = {
            "number": number[0],
            "name": name,
            "status": status,
        }
        yield PepParseItem(data)
