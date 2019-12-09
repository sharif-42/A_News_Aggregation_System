from django.contrib import admin
from bangla.models import BanglaNews


class NewsAdmin(admin.ModelAdmin):
    search_fields = ['id','news_paper_name','news_category']
    list_display = ('id','headline', 'news_paper_name','news_category','publish_time')

admin.site.register(BanglaNews, NewsAdmin)
