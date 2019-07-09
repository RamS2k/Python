from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "current_time" : strftime("%Y-%m-%d %H:%M %p", gmtime()),
        
    }
    return render(request, 'blogs/index.html', context)
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    return redirect('/')
def show(request, number):
    response = "placeholder to display blog "
    return HttpResponse(response + number)
def edit(request, year):
    response = "placeholder to edit blog "
    return HttpResponse(response + year)
def destroy(request, number):
    return redirect('/')

