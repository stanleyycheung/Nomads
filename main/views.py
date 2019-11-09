from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from main.forms import HomeForm
from django.shortcuts import render

from .models import Personality, TripCategories

# Create your views here.

def main(request):
    if request.method == 'POST':
        personalites = []
        # location = request.POST.get('')
        # form = HomeForm(request.POST)
        # if form.is_valid():
        #     home_location = form.cleaned_data['location']
        #     print(home_location)

        myCountry = request.POST['myCountry']

        checked = request.POST.getlist('checks')

        print(checked)

        print(myCountry)

        return render(request, 'main/index.html')

    elif request.method == 'GET':
        # loc_form = HomeForm()
        template = loader.get_template('main/index.html')
        # return HttpResponse(template.render('form': form))
        context = {}
        return render(request, 'main/index.html')
        # return render(request, 'main/index.html', {'loc_form': loc_form})

def personality(request, user_id):
    user_personality = Personality.objects.all()
    template = loader.get_template('main/index.html')
    context = {
        'user_personality' : user_personality,
    }
    return HttpResponse(template.render(context, request))

def categories(request, user_id):
    response = "You are looking at %s Category."
    return HttpResponse(response % user_id)

def results(request, user_id):
    template = template.render('main/results.html')

    return HttpResponse(template.render())

def locations(request):
    template = loader.get_template('main/locations.html')

    return HttpResponse(template.render())
