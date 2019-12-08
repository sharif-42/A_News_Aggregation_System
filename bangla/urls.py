from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name="bangla/home"),
    # path('national/', views.national, name="bangla/national"),
    path('sports/', views.SportsApi.as_view(), name="bangla/sports"),
    # path('politics/', views.politics, name="bangla/politics"),
    # path('technology/', views.technology, name="bangla/technology"),
    # path('entertainment/', views.entertainment, name="bangla/entertainment"),
    # path('international/', views.international, name="bangla/international"),
    #
    # path('about_us/', views.about_us, name='bangla/about_us'),

]