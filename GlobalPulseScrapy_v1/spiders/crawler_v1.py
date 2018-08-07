# -*- coding: utf-8 -*-
import logging
import scrapy
import json
import pandas as pd
from urllib.request import urlopen
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from items import jsonitem, csvitem, txtitem, datitem, xlsitem, linkitem
from InputLinks import input_links

# need to work on .dat .data .xls .xlsx
# scrapy callback from parse function

class crawler_v1(CrawlSpider):
    name = "crawler_v1"
    allowed_domains = []
    start_urls = input_links.start_urls

    # get response from extracted links
    rules = [
        Rule(LinkExtractor(allow = ".json", canonicalize=True, unique=True), follow=False, callback="parse_json"),
        Rule(LinkExtractor(allow = ".csv", canonicalize=True, unique=True), follow=False, callback="parse_csv"),
        Rule(LinkExtractor(allow = ".txt", canonicalize=True, unique=True), follow=False, callback="parse_txt"),
        Rule(LinkExtractor(allow = (".dat", ".data"), canonicalize=True, unique=True), follow=False, callback="parse_dat"),
        Rule(LinkExtractor(allow = ".xls", canonicalize=True, unique=True), follow=False, callback="parse_xls"),
        Rule(LinkExtractor(allow = "", deny = (".json", ".csv", ".txt", ".dat", ".data"), canonicalize=True, unique=True), follow=False, callback="parse_link"),
    ]

    def parse_json(self, response):
        json_item = jsonitem()
        json_item["file_link"] = response.url
        json_item["json_file"] = json.loads(response.body_as_unicode())
        return json_item

    def parse_csv(self, response):
        logging.info(response.url)
        csv_item = csvitem()
        csv_item["file_link"] = response.url
        csv_item["csv_file"] = pd.read_csv(response.url).to_json(orient="split")
        return csv_item

    def parse_txt(self, response):
        logging.info(response.url)
        #if response.url.endswith(".txt"):
        txt_item = txtitem()
        txt_item["file_link"] = response.url
        txt_item["txt_file"] = urlopen(response.url).read().decode('utf-8')
        return txt_item
        #else:
        #    add_link = linkitem()
        #    links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        #    for link in links:
        #        add_link["parent_link"] = response.url
        #        add_link["link_url"] = link.url
        #    yield add_link

    def parse_dat(self, response):
        logging.info(response.url)
        #if response.url.endswith((".data",".dat")):
        dat_item = datitem()
        dat_item["file_link"] = response.url
        dat_item["dat_file"] = urlopen(response.url).read().decode('utf-8')
        return dat_item
        #else:
        #    add_link = linkitem()
        #    links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        #    for link in links:
        #        add_link["parent_link"] = response.url
        #        add_link["link_url"] = link.url
        #    yield add_link

    def parse_xls(self, response):
        logging.info(response.url + "as excel file")
        xls_item = xlsitem()
        xls_item["file_link"] = response.url
        xls_item["xls_file"] = pd.read_excel(response.url).to_json(orient="split")
        return xls_item

    def parse_link(self, response):
        # The list of items that are found on the particular page
        add_link = linkitem()
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        # Now go through all the found links
        for link in links:
            add_link['parent_link'] = response.url
            add_link['link_url'] = link.url
        # Return all the found items
        yield add_link
