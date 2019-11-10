from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode

from main.utils import get_locations, get_flights, parse

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

        request.session['destinations'] = get_locations(request.session['personalities'])
        print(request.session['destinations'])
        return render(request, 'main/locations.html')

    elif request.method == "POST":

        budget = request.POST['bdg']
        dates = request.POST['daterange']
        # print(dates + '\n\n\n\n')

        depDate = "{}-{}-{}".format(dates[6:10], dates[0:2], dates[3:5])
        retDate = "{}-{}-{}".format(dates[-4:], dates[-10:-8], dates[-7:-5])

        total_price, deperature_time, arrival_time, travel_class, carrier_code = parse(org=request.session['location']
        , dest='LON', depDate=depDate)

        request.session['total_price'] = total_price
        request.session['departure_time'] = departure_time
        request.session['arrival_time'] = arrival_time
        request.session['travel_class'] = travel_class
        request.session['carrier_code'] = carrier_code

        return render(request, 'main/locations.html')

def results(request, user_id):

    if request.method == "GET":

        rows = list(zip(request.session['total_price'], request.session['departure_time'], request.session['arrival_time'], request.session['travel_class'], request.session['carrier_code']))

        return HttpResponse(template.render())
