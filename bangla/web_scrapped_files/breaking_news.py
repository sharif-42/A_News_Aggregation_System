import requests
from bs4 import BeautifulSoup


class BreakingNews:
    def __init__(self):
        self.news = []

    def get_bdnews_breaking_news(self):
        r = requests.get('https://bangla.bdnews24.com/')
        soup = BeautifulSoup(r.text, 'html.parser')
        r = soup.find_all('h6', attrs={'class': 'default'})
        return r

    def get_bbc_breaking_news(self):
        r = requests.get('https://www.bbc.com/bengali')
        soup = BeautifulSoup(r.text, 'html.parser')
        r = soup.find_all('div', attrs={'class': "dove-item__body"})
        return r

    def get_prothom_alo_news(self):
        r = requests.get('http://www.prothomalo.com/')
        soup = BeautifulSoup(r.text, 'html.parser')
        r1 = soup.find_all('div', attrs={'class': 'col col1'})
        return r1

    def get_breaking_news(self):
        bdnews = self.get_bdnews_breaking_news()
        bbc_news = self.get_bbc_breaking_news()
        prothom_alo_news = self.get_prothom_alo_news()

        # l = 0
        # for n in prothom_alo_news:
        #     print(n)
        #     if l < 12:
        #         url = 'http://www.prothomalo.com/' + n.find('a')['href']
        #         t = n.find('h2')
        #         txt = t.find('span').text
        #         self.news.append((txt, url, 'prothom alo'))
        #     l += 1


        # for news in bbc_news:
        #     t = news.find('a')
        #     txt = t.find('h3').text[1:-1]
        #     url = 'https://www.bbc.com'# + news.find('a')['href']
        #     news.append((txt, url, 'BBC-bangla'))

        for n in bdnews:
            url = n.find('a')['href']
            text = n.find('a').text[1:-1]
            self.news.append((text, url, 'Bdnews24.com'))
        return self.news
