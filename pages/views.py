from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing, Realtor

def index(request):
    listings = Listing.objects.order_by('-list_data').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get realtor
    realtors = Realtor.objects.order_by('-hire_data')
    # Get mvp realtor
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)




