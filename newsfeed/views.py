from django.shortcuts import render
from django.http import JsonResponse
import requests
import feedparser

# Create your views here.
# Main page of app.


def index(request):
    # parse xml feed
    newsfeed = feedparser.parse("https://www.sciencedaily.com/rss/space_time/mars.xml")

    # News list for storage.
    news = []

    # Store the rss feed items to the news list.
    for entry in newsfeed.entries:
        items = {'title': entry.title, 'link': entry.link, 'date': entry.published,
                 'time': entry.published_parsed, 'summary': entry.summary}
        news.append(items)

    return render(request, 'news.html', {'news': news})
