from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode

from main.personality import get_location

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

    if request.method == "GET":

        print(request.session['location'] + " is home city")
        print(request.session['personalities'])

        get_location(request.session['personalities'])

        request.session['destinations'] = ['LON', 'JPN', 'HKG']
        return render(request, 'main/locations.html')

    elif request.method == "POST":

        budget = request.POST['bdg']
        dates = request.POST['daterange']
        # print(dates + '\n\n\n\n')

        depDate = "{}-{}-{}".format(dates[6:10], dates[0:2], dates[3:5])
        retDate = "{}-{}-{}".format(dates[-4:], dates[-10:-8], dates[-7:-5])

        return render(request, 'main/locations.html')

def results(request, user_id):

    if request.method == "GET":
        return HttpResponse(template.render())
