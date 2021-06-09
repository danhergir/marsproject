from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests


# Create your views here.
# Main page of app.
def index(request):
    response = requests.get('https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0')
    latest_weather = response.json()

    #return render(request, "weather/display.html", {"latest_weather": latest_weather})
    return JsonResponse({'latest_weather': latest_weather})