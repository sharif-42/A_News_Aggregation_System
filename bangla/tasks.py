from celery import shared_task

from bangla.models import BanglaNews


@shared_task
def get_sports_news():
    BanglaNews.objects.insert_sports_news()


@shared_task
def get_national_news():
    BanglaNews.objects.insert_national_news()
    pass


@shared_task
def get_political_news():
    pass


@shared_task
def get_international_news():
    pass


@shared_task
def get_entertainment_news():
    pass


@shared_task
def get_technology_news():
    pass


@shared_task
def get_mostread_news():
    pass
