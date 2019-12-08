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
        post = BanglaNews.objects.all()
        h1 = "Breaking news"
        h2 = "Most popular"
        return Response({'h1':h1,'h2':h2,'post':post,'post':post}, status=status.HTTP_200_OK)