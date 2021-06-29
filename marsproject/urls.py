# Django
from marsproject import calculator
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

#from marsproject import views as local_views
from . import views
from .calculator import views as calculator_views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('rovers/', views.index),

    path('home/', views.home),

    path('mars/', views.mars),

    path('calculator/', calculator_views.calculate, name='calculator-calculate'),
    #path('', rovers_views.index, name='index'),

    path('weather/', include('weather.urls')),

    path('newsfeed/', include('newsfeed.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
