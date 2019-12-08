from django.contrib import admin
from english.models import EnglishNews


class NewsAdmin(admin.ModelAdmin):
    search_fields = ['id','news_paper_name','news_category']
    list_display = ('id', 'news_paper_name','news_category','publish_time')

admin.site.register(EnglishNews, NewsAdmin)
