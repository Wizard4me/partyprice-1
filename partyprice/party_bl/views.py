# coding=UTF-8
from django.shortcuts import render
from dajaxice.core import dajaxice_functions
# Create your views here.


def index(request):
    return render(request, 'party_bl/index.html')

def report(request):
    return render(request, 'party_bl/report.html')

def event(request):
    return render(request, 'party_bl/event.html')

