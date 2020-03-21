from django.contrib import admin

from .models import BanglaNews


@admin.register(BanglaNews)
class BanglaNewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'news_paper_name',
        'headline',
        'url',
        'news_category',
        'publish_time',
        'summary',
    )
    list_filter = ('publish_time',)
