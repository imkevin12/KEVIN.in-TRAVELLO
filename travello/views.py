from django.shortcuts import render
from .models import Destination


def index(request):
    destinations = Destination.objects.all()
    return render(request, "index.html", {'destinations': destinations})


def about(request):
    return render(request, 'about.html')


def services(request):
    destinations = Destination.objects.all()
    return render(request, "services.html", {'destinations': destinations})


def news(request):
    return render(request, 'news.html')


def contact(request):
    return render(request, 'contact.html')
