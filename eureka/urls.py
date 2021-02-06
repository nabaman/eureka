from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginView , name='login'),
    path('logout/',logoutView,name='logout'),
    path('dashboard/',include('learning.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)