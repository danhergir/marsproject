from django.urls import path
from . import views

# URL configuration
urlpatterns = [
    # Pass reference to function instead of calling.
    path('', views.index, name='index'),
]