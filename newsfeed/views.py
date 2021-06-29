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

    news = {}
    entry_name = 'entry'
    count = 0

    for entry in newsfeed.entries:
        items = {'title': entry.title, 'link': entry.link, 'date': entry.published,
                 'time': entry.published_parsed, 'summary': entry.summary}
        news.append(items)

        count += 1

    return render(request, 'newsfeed.html', {'news': news})