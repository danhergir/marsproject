"""Posts views."""

# Django
from django.shortcuts import render

# Utilities
from datetime import datetime
import requests

def index(request):
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY'
    response = requests.get(url)
    data = response.json()
    posts = data['photos']

    return render(request, 'home.html', {'posts': posts})

