from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'surveys/index.html')
def create(request):
    context = {
        "name" : request.POST['name'],
        "email" : request.POST['email'],
        "dojo" : request.POST['dojo_location'],
        "language" : request.POST['favorite_language']
    }
    return render(request, 'surveys/results.html', context)
