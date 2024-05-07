import scrapy
from scrapy.crawler import CrawlerProcess
from wiki_crawler import WikiCrawler


def main():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(WikiCrawler)
    process.start()


if __name__ == '__main__':
    main()
