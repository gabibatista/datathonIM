#!/bin/bash -xe

scrapy runspider clutch_spider.py -s HTTPCACHE_ENABLED=0 -o companies.csv
