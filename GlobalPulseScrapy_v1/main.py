# -*- coding: utf-8 -*-

# importing required packages
import logging

# import scrapy packages
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# importing scrapy spiders
from spiders.crawler_v1 import crawler_v1


# main function
def main():

    '''
    description of overall scrapy program
    '''

    # configuring log settings
    logging.basicConfig(filename="main.log", filemode = "w", format="%(asctime)s%(levelname)s:%(message)s", level=logging.DEBUG)

    # import project settings
    process = CrawlerProcess(get_project_settings())

    # running first crawler
    process.crawl(crawler_v1)
    process.start()
    logging.info("crawler_v1 finished crawling")
    process.stop()

    


if __name__=='__main__':
    main()
