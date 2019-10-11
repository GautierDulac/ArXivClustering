"""
Created on Thu Mar 28 13:50:39 2019

@author: liangkc
"""

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
        queries = ['cat:econ.EM', 'cat:econ.TH', 'econ.GN', 'q-fin.ST', 'q-fin.TR', 'q-fin.EC']
        start = time.time()
        with open('./data/arxiv-paper-titles-data-abstracts.csv', mode='w', newline="") as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for query in queries:
                print("Category in process : " + query)
                num = 0
                for chunk_i in range(0, 2000, chunk_size):
                    feed = feedparser.parse(
                        'http://export.arxiv.org/api/query?search_query=%s&start=%d&max_results=%d' % \
                        (query, chunk_i, chunk_size))
                    for i in range(len(feed.entries)):
                        entry = feed.entries[i]
                        article_id = entry.id
                        title = entry.title.replace('\n', " ").replace(';',' ')
                        published = entry.published
                        author = entry.author
                        abstract = entry.summary.replace('\n', " ").replace(';', ' ')
                        file_writer.writerow([unidecode(article_id), unidecode(title), unidecode(published),
                                              unidecode(author), unidecode(abstract)])
                        num = num + 1
                    print(str(num) + " article : " + title)
                print('%d titles saved from Arxiv %s.' % (num, query))

        end = time.time()
        print('Time elapsed: %s' % datetime.timedelta(seconds=round(end - start)))
        data_file.close()
