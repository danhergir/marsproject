from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests


# Create your views here.
# Main page of app.
def index(request):
    response = requests.get('https://mars.nasa.gov/rss/api/?feed=weather&category=mars2020&feedtype=json')
    latest_weather = response.json()

    # Remove ls from dictionary, undocumented value.
    if 'ls' in latest_weather:
        del latest_weather['ls']

    #return render(request, "weather/display.html", {"latest_weather": latest_weather})
    return JsonResponse({'latest_weather': latest_weather})