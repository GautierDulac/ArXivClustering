"""
Created on Thu Mar 28 13:50:39 2019

@author: liangkc
"""

# you need to install Biopython:
# pip install biopython

# Full discussion:
# https://marcobonzanini.wordpress.com/2015/01/12/searching-pubmed-with-python/

import csv
import time
import datetime
import feedparser
from unidecode import unidecode


def main_arxivscrapper(run_loading=False):
    if run_loading:
        chunk_size = 50
        # ARXIV QUERY
        queries = ['econ']
        start = time.time()
        with open('arxiv-paper-titles-data-abstracts.csv', mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for query in queries:
                num = 0
                for chunk_i in range(0, 20000, chunk_size):
                    feed = feedparser.parse(
                        'http://export.arxiv.org/api/query?search_query=%s&start=%d&max_results=%d' % \
                        (query, chunk_i, chunk_size))
                    print(feed)

                    for i in range(len(feed.entries)):
                        entry = feed.entries[i]
                        article_id = entry.id
                        title = entry.title.replace('\n', " ")
                        published = entry.published
                        author = entry.author
                        abstract = entry.summary.replace('\n', " ")
                        file_writer.writerow([unidecode(article_id), unidecode(title), unidecode(published),
                                              unidecode(author), unidecode(abstract), str(0)])
                        num = num + 1
                print('%d titles saved from Arxiv %s.' % (num, query))

        end = time.time()
        print('Time elapsed: %s' % datetime.timedelta(seconds=round(end - start)))
        data_file.close()
