from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode

from .models import Personality, TripCategories

# Create your views here.

PERSCODE = {'Shopaholic': 1, 'Everything': 2, 'Foodie': 3, 'Touristy': 4, 'Outdoor': 5, 'Chill': 6}

def main(request):
    if request.method == 'POST':

        home = request.POST['myCountry']
        personalities = request.POST.getlist('checks')

        request.session['location'] = home
        request.session['personalities'] = personalities

        return redirect('locations/')

    elif request.method == 'GET':
        return render(request, 'main/index.html')

def locations(request):

    print(request.session['location'] + " is home city")
    print(request.session['personalities'])

    
    return render(request, 'main/locations.html')

def categories(request, user_id):
    response = "You are looking at %s Category."
    return HttpResponse(response % user_id)

def results(request, user_id):
    template = template.render('main/results.html')

    return HttpResponse(template.render())
