# -*- coding: utf-8 -*-
import scrapy
import json
#from ftcodes import urls, tickers
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.abspath(os.path.join(base_dir, "ftcodes.txt"))

class FtSpiderSpider(scrapy.Spider):
    name = 'ft_spider'
    allowed_domains = ['ft.com']
    #start_urls = ['https://markets.ft.com/data/equities/ajax/get-historical-prices?startDate=2018%2F03%2F01&endDate=2018%2F03%2F09&symbol=254084']
    start_urls = []

    base_url = 'https://markets.ft.com/data/equities/ajax/get-historical-prices?startDate=2018%2F03%2F01&endDate=2018%2F03%2F09&symbol={}'

    with open(file_path) as f:
        ftcodes = [ftcode.replace("\n","") for ftcode in f.readlines()]

    ftcodes = ftcodes[:5]

    for ftcode in ftcodes:
        temp_url = base_url.format(ftcode)
        start_urls.append(temp_url)


    def parse(self, response):
        #self.log(response.url)
        #self.log(response.text)
        data = json.loads(response.text)

        yield{
            "data":data["html"],
            "url":response.request.url,
            }
