from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.htm')

def about(request):
    return render(request, 'pages/about.htm')




