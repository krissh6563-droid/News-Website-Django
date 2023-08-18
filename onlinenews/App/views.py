from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    import requests
    import json

    news_api_request = requests.get(
        "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f7ad1839025e4eec8d50df738378826a")

    api = json.loads(news_api_request.content)

    return render(request, 'home.html', {'api': api})
