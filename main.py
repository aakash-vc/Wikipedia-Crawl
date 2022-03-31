import os
from src.crawl import Crawl
from src.process import Process
from src.graph import Graph


if __name__ == '__main__':

    url = 'https://en.wikipedia.org/wiki/Batman' #input('Enter URL: ')
    lst = Crawl.input_url(url)
    df = Crawl.get_connections(lst)

    print(df)

    if not os.path.exists('data/connections.csv'):
        with open('data/connections.csv', 'w') as file:
            pass
    if not os.stat('data/connections.csv').st_size == 0:
        df = Process.merge_dataframes(df)
    df.to_csv('data/connections.csv', index=False)

    Graph.graph()