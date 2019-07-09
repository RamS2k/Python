from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
import re
from .models import *
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

def index(request):
    if 'id' not in request.session:
        request.session['id'] = ""
    return render(request, 'lognreg/index.html')
def register(request):
    hasErrors = Person.objects.person_val(request.POST)
    if len(hasErrors) > 0:
        for error in hasErrors:
            messages.error(request, hasErrors[error])
        return redirect('/lognreg')
    else:
        try:
            Person.objects.get(email = request.POST['email'])
            messages.error(request, "Email already taken")
            return redirect('/lognreg')
        except:
            the_person = Person.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
            request.session['id'] = the_person.id
            return redirect('/lognreg/success')
def login(request):
    try:
        the_person = Person.objects.get(email = request.POST['email'])
        if request.POST['password'] == the_person.password:
            request.session['id'] = the_person.id
            return redirect('/lognreg/success')
        else:
            messages.error(request, "Invalid password")
            return redirect('/lognreg')
    except:
        messages.error(request, "Email not found")
        return redirect('/lognreg')
def success(request):
    person_data = {
        'current_person' : Person.objects.get(id = request.session['id'])
    }
    return render(request, 'lognreg/success.html', person_data)