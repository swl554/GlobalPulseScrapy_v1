# -*- coding: utf-8 -*-

import logging
import scrapy
from scrapy.exporters import JsonLinesItemExporter, JsonItemExporter
from items import jsonitem, csvitem, txtitem, datitem, xlsitem, linkitem


class JsonPipeline(object):
    def __init__(self):
        self.file = open("OutputJson.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if not isinstance(item, jsonitem):
            return item
        self.exporter.export_item(item)
        logging.info("link item processed through JsonPipeline")
        return item

class CsvPipeline(object):
    def __init__(self):
        self.file = open("OutputCsv.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if not isinstance(item, csvitem):
            return item
        self.exporter.export_item(item)
        logging.info("link item processed through CsvPipeline")
        return item

class TxtPipeline(object):
    def __init__(self):
        self.file = open("OutputTxt.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if not isinstance(item, txtitem):
            return item
        self.exporter.export_item(item)
        logging.info("link item processed through TxtPipeline")
        return item

class DatPipeline(object):
    def __init__(self):
        self.file = open("OutputDat.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if not isinstance(item, datitem):
            return item
        self.exporter.export_item(item)
        logging.info("link item processed through DatPipeline")
        return item

class XlsPipeline(object):
    def __init__(self):
        self.file = open("OutputXls.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if not isinstance(item, xlsitem):
            return item
        self.exporter.export_item(item)
        logging.info("link item processed through XlsPipeline")
        return item

class LinkPipeline(object):
    def __init__(self):
        self.file = open("OutputLinks.json", 'ab')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if not isinstance(item, linkitem):
            return item
        self.exporter.export_item(item)
        logging.info("link item processed through LinkPipeline")
        return item
