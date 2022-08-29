from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    searchCity = request.GET.get('searchCity')
    return render(request, 'home.html', {'searchCity': searchCity})
