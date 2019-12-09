import requests
from bs4 import BeautifulSoup


class MostReadNews:
    def __init__(self):
        self.news = []

    def get_bdnews_most_read_news(self):
        r = requests.get('https://bangla.bdnews24.com/politics/')
        soup = BeautifulSoup(r.text, 'html.parser')
        r1 = soup.find_all('li', attrs={'class': 'article first '})
        r2 = soup.find_all('li', attrs={'class': 'article '})
        print(r1,r2)
        return r1 + r2

    def get_most_read_news(self):
        bdnews = self.get_bdnews_most_read_news()

        l = 0
        for news in bdnews:
            if l == 9:
                break
            l += 1
            url = news.find('a')['href']
            text = news.find('a').text[1:-1]
            self.news.append((text, url, 'Bdnews24.com'))
        return self.news
