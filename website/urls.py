from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bangla/', include('bangla.urls')),
    path('english/', include('english.urls')),
]