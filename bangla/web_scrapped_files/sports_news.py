import requests
from bs4 import BeautifulSoup


class SportsNews:
    def __init__(self):
        self.news = []

    def get_bdnews_sports_news(self):
        r = requests.get('https://bangla.bdnews24.com/sport/')
        soup = BeautifulSoup(r.text, 'html.parser')
        r1 = soup.find_all('div', attrs={'class': 'text'})
        return r1

    def get_jugantor_sports_news(self):
        r = requests.get('https://www.jugantor.com/sports')
        soup = BeautifulSoup(r.text, 'html.parser')
        r2 = soup.find_all('div', attrs={'class': "leadimg"})
        return r2

    def get_sports_news(self):
        bdnews = self.get_bdnews_sports_news()
        jugantor_news = self.get_jugantor_sports_news()

        l = 0
        for news in bdnews:
            if l == 6:
                break
            l += 1
            url = news.find('a')['href']
            text = news.find('a').text[1:-1]
            self.news.append((text,url, 'Bdnews24.com'))

        for news in jugantor_news:
            if l == 12:
                break
            l += 1
            url = news.find('a')['href']
            txt = news.find('a').text[2:-1]
            self.news.append((txt, url, 'যুগান্তর'))
        return self.news
