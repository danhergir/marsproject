# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

#from marsproject import views as local_views
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('rovers/', views.index),
    #path('', rovers_views.index, name='index'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
