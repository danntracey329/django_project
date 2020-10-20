from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Dan Tracey",
        "title": "First Post",
        "content": "First content",
        "date_posted": "October 19, 2020",
    },
    {
        "author": "Lily Tracey",
        "title": "Second Post",
        "content": "Second content",
        "date_posted": "October 20, 2020",
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
