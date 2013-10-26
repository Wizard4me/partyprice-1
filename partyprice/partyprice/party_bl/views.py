# coding=UTF-8
#тестовый коммит
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'party_bl/index.html')

def event(request):
    return render(request, 'party_bl/event.html')

def report(request):
    return render(request, 'party_bl/report.html')