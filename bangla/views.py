from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from bangla.models import BanglaNews


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        #BanglaNews.objects.insert_sports_news()
        mst = BanglaNews.objects.filter(news_category = 'Sports')
        post = BanglaNews.objects.all()
        h1 = "সর্বশেষ খবর"
        h2 = "সর্বাধিক পঠিত"
        return Response({'h1':h1,'h2':h2,'post':post,'pst':mst}, status=status.HTTP_200_OK)

class SportsApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self,request):
        #BanglaNews.objects.insert_sports_news()
        post = BanglaNews.objects.filter(news_category = 'Sports')
        h1 = "Sports News"
        h2 = "Most Read News"
        return Response({'h1':h1,'h2':h2,'post':post,'post':post}, status=status.HTTP_200_OK)

class NationalNewsApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self,request):
        #BanglaNews.objects.insert_national_news()
        national_news = BanglaNews.objects.filter(news_category = 'National')
        #national_news = BanglaNews.objects.filter(news_category = 'National')
        h1 = "National News"
        h2 = "Most Read News"
        return Response({'h1':h1,'h2':h2,'post':national_news,'post':national_news}, status=status.HTTP_200_OK)

class MostReadNewsApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self,request):
        #BanglaNews.objects.insert_national_news()
        national_news = BanglaNews.objects.filter(news_category = 'National')
        #national_news = BanglaNews.objects.filter(news_category = 'National')
        h1 = "National News"
        h2 = "Most Read News"
        return Response({'h1':h1,'h2':h2,'post':national_news,'post':national_news}, status=status.HTTP_200_OK)