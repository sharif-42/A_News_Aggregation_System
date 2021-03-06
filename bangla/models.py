from django.db import models

from bangla.web_scrapped_files.breaking_news import BreakingNews
from bangla.web_scrapped_files.sports_news import SportsNews
from bangla.web_scrapped_files.national_news import NationalNews
from bangla.web_scrapped_files.most_read_news import MostReadNews


class BanglaNewsManager(models.Manager):
    def insert_sports_news(self):
        sports_news = SportsNews()
        news = sports_news.get_sports_news()
        objs = [
            BanglaNews(
                news_paper_name=n[2],
                headline=n[0],
                url=n[1],
                news_category='Sports',
            )
            for n in news
        ]
        BanglaNews.objects.bulk_create(objs)

    def insert_national_news(self):
        national_news = NationalNews()
        news = national_news.get_national_news()
        objs = [
            BanglaNews(
                news_paper_name=n[2],
                headline=n[0],
                url=n[1],
                news_category='National',
            )
            for n in news
        ]
        BanglaNews.objects.bulk_create(objs)

    def insert_most_read_news(self):
        most_read_news = MostReadNews()
        news = most_read_news.get_most_read_news()
        print(news)
        objs = [
            BanglaNews(
                news_paper_name=n[2],
                headline=n[0],
                url=n[1],
                news_category='Most Read',
            )
            for n in news
        ]
        print("done")
        BanglaNews.objects.bulk_create(objs)

    def insert_breaking_news(self):
        breaking_news = BreakingNews()
        news = breaking_news.get_breaking_news()
        print(news)
        objs = [
            BanglaNews(
                news_paper_name=n[2],
                headline=n[0],
                url=n[1],
                news_category='Breaking News',
            )
            for n in news
        ]
        print("done")
        BanglaNews.objects.bulk_create(objs)

class BanglaNews(models.Model):
    MOST_READ = 'Most Read'
    BREAKING_NEWS = 'Breaking News'
    NATIONAL = 'National'
    INTER_NATIONAL = 'Inter National'
    POLITICS = 'Politics'
    SPORTS = 'Sports'
    ENTERTAINMENT = 'Entertainment'
    TECHNOLOGY = 'Technology'

    CATEGORY = [
        (MOST_READ, 'Most Read'),
        (BREAKING_NEWS, 'Breaking News'),
        (NATIONAL, 'National'),
        (INTER_NATIONAL, 'Inter National'),
        (POLITICS, 'Politics'),
        (SPORTS, 'Sports'),
        (ENTERTAINMENT, 'Entertainment'),
        (TECHNOLOGY, 'Technology'),
    ]
    id = models.BigAutoField(primary_key=True, db_index=True)
    news_paper_name = models.CharField(max_length=100)
    headline = models.CharField(max_length=500)
    url = models.URLField()
    news_category = models.CharField(max_length=20, choices=CATEGORY, default=MOST_READ)
    publish_time = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length=2000, null=True, blank=True)
    objects = BanglaNewsManager()

    def __str__(self):
        return '{} -- {}'.format(self.news_category, self.news_paper_name)

    class Meta:
        indexes = [
            models.Index(fields=['id', 'news_category', 'news_paper_name', 'publish_time']),
            # models.Index(fields=['first_name'], name='first_name_idx'),
        ]
        verbose_name = "Bangla Newspaper"
        verbose_name_plural = "Bangla Newspapers"
