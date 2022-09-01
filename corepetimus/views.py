from django.shortcuts import render
from django.http import HttpResponse
from .models import Petimus, Image

def home(request):
    if request.GET.get('searchCity'):
        searchCity = request.GET.get('searchCity')
        petimus = Petimus.objects.filter(city__icontains=searchCity)
        images = ''
        for p in petimus:
            images=p.petimus_images.all()
        return render(request, 'home.html', 
            {'searchCity': searchCity, 'petimus': petimus})
    else:
        return render(request, 'home.html')        
