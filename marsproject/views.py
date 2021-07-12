"""Posts views."""

# Django
from django.shortcuts import render

# Utilities
from datetime import datetime
import requests

def index(request):
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/photos?sol=10&api_key=HADRCHX7UmA6MpuOkl7vUXs3QXwifDyR239GU67I'
    response = requests.get(url)
    data = response.json()
    posts = data['photos']

    return render(request, 'home.html', {'posts': posts})

def home(request):
    return render(request, 'home-template.html')

def mars(request):
    return render(request, 'mars.html')




