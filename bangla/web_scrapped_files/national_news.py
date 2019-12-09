import requests
from bs4 import BeautifulSoup


class NationalNews:
    def __init__(self):
        self.news = []

    def get_bdnews_sports_news(self):
        r = requests.get('https://bangla.bdnews24.com/samagrabangladesh/')
        soup = BeautifulSoup(r.text, 'html.parser')
        r1 = soup.find_all('h6', attrs={'class': 'default'})
        r2 = soup.find_all('h1', attrs={'class': 'default'})
        return r1 + r2

    def get_jugantor_national_news(self):
        r = requests.get('https://www.jugantor.com/national')
        soup = BeautifulSoup(r.text, 'html.parser')
        r2 = soup.find_all('div', attrs={'class': "leadmorehl2"})
        return r2

    def get_bangla_tribune_national_news(self):
        r = requests.get('https://bangla.dhakatribune.com/articles/bangladesh')
        soup = BeautifulSoup(r.text, 'html.parser')
        r1 = soup.find_all('div', attrs={'class': 'top-news-cont list-para'})
        r2 = soup.find_all('h4', attrs={'class': 'news-title'})

    def get_national_news(self):
        bdnews = self.get_bdnews_sports_news()
        jugantor_news = self.get_jugantor_national_news()
        l = 0
        for news in bdnews:
            if l == 6:
                break
            l += 1
            url = news.find('a')['href']
            text = news.find('a').text[1:-1]
            self.news.append((text, url, 'Bdnews24.com'))

        for news in jugantor_news:
            if l == 12:
                break
            l += 1
            url = news.find('a')['href']
            txt = news.find('a').text[1:-1]
            self.news.append((txt, url, 'যুগান্তর'))

        return self.news
