from django.db import models


class EnglishNews(models.Model):
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

    def __str__(self):
        return '{} -- {}'.format(self.news_category, self.news_paper_name)

    class Meta:
        indexes = [
            models.Index(fields=['id', 'news_category', 'news_paper_name', 'publish_time']),
            # models.Index(fields=['first_name'], name='first_name_idx'),
        ]
        verbose_name = "English Newspaper"
        verbose_name_plural = "English Newspapers"
