# Django
from marsproject import calculator
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

#from marsproject import views as local_views
from . import views
from .calculator import views as calculator_views


urlpatterns = [

    path('admin/', admin.site.urls,),

    path('rovers/', views.index, name="rovers"),

    path('home/', views.home, name="home"),

    path('mars/', views.mars, name="mars"),

    path('calculator/', calculator_views.calculate, name='calculator-calculate'),
    #path('', rovers_views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
