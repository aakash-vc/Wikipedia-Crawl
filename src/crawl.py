import time
import requests
from bs4 import BeautifulSoup

class Crawl:

    def __init__(self):
        pass

    def crawl(self, search_history, target):
        # Checking if the latest url matches the target url
        if search_history[-1] == target:
            print("\nReached Target")
            return False
        # Terminating in case the chain is too long
        elif len(search_history) >= 30:
            print("Overload")
            return False
        # Terminating in case the crawl enters a loop by checking for duplicate elements
        elif len(set(search_history)) < len(search_history):
            print("Looping")
            return False
        else:
            return True


    def get_next(self, search_history):
        req_url  = search_history[-1]
        response = requests.get(req_url).text
        soup = BeautifulSoup(response, 'html.parser')
        div_tag = soup.find("div", {"id": "bodyContent"})
        for b in div_tag('b'):
            b.decompose()

        a_tags = div_tag.select('p a')        

        for i in range(len(a_tags)):
            if a_tags[i].get('href').startswith('/wiki/Help:IPA/'):
                continue
            if a_tags[i].get('href').startswith('/wiki/File:'):
                continue
            if a_tags[i].parent.name == 'small':
                continue
            if a_tags[i].get('href').startswith('#cite_note'):
                continue
            #if a_tags[i].attrs.get('class') and a_tags[i].attrs.get('class')[0]=='mw-redirect':
            #    continue

            next = a_tags[i].get('href')
            print('next: ', next)
            break
        return next



    def input_url(self, url):
        target_url = 'https://en.wikipedia.org/wiki/Philosophy'
        search_history = [url]

        while self.crawl(search_history, target_url):
            next = self.get_next(search_history)
            search_history.append('https://en.wikipedia.org'+next)
            time.sleep(1)

        return search_history