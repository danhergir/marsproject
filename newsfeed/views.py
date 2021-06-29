from django.shortcuts import render
from django.http import JsonResponse
import requests
import webbrowser
import feedparser

# Create your views here.
# Main page of app.
def index(request):
    # parse xml feed
    newsfeed = feedparser.parse("https://www,sciencedaily.com/rss/space_time/mars.xml")

    items = {}


    for entry in newsfeed.entries:
        title = entry.title
        link = entry.link
        date = entry.published
        summary = entry.summary

    return