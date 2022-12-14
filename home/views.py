from django.shortcuts import render

from .models import Event

# Create your views here.

def home(request):
    eventData = Event.objects.all().order_by('date')[:3]
    return render(request , 'home.html', {'active': 'home', 'events':eventData})

def events(request):
    upcomingEventData = Event.objects.filter(status='UE')
    pastEventData = Event.objects.filter(status='PE')

    return render(request , 'events.html', {'active': 'home', 'pevents':pastEventData, 'uevents':upcomingEventData})

def archive(request):
    return render(request , 'archive.html', {'active': 'archive'})

def about(request):
    return render(request , 'about.html', {'active': 'about'})