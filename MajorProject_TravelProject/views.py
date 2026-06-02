"""from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def explore(request):
    return render(request,'explore.html')


def mood(request):
    return render(request, 'mood.html')

def login(request):
    return render(request,'login.html')

def gallery(request):
    return render(request,'gallery.html')

def wishlist(request):
    return render(request,'wishlist.html')

def bookings(request):
    return render(request,'bookings.html')

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def map(request):
    return render(request,'map.html')

def adminpanel(request):
    return render(request,'adminpanel.html')"""
"""
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')"""

from django.shortcuts import render
from .models import Traveler

def home(request):

    if request.method == 'POST':

        Traveler.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            destination=request.POST.get('destination'),
            budget=request.POST.get('budget'),
            mood=request.POST.get('mood')
        )

    return render(request, 'home.html')