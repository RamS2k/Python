from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
import re
from .models import *
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

def index(request):
    if 'id' not in request.session:
        request.session['id'] = ""
    return render(request, 'helper/index.html')
def register(request):
    hasErrors = Users.objects.user_val(request.POST)
    if len(hasErrors) > 0:
        for error in hasErrors:
            messages.error(request, hasErrors[error])
        return redirect('/helper')
    else:
        try:
            Users.objects.get(email = request.POST['email'])
            messages.error(request, "Email already taken")
            return redirect('/helper')
        except:
            the_user = Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
            request.session['id'] = the_user.id
            return redirect('/helper/load_dash')
def login(request):
    try:
        the_user = Users.objects.get(email = request.POST['email'])
        if request.POST['password'] == the_user.password:
            request.session['id'] = the_user.id
            return redirect('/helper/load_dash')
        else:
            messages.error(request, "Invalid password")
            return redirect('/helper')
    except:
        messages.error(request, "Email not found")
        return redirect('/helper')
def load_dash(request):
    user_data = {
        'user_jobs' : Job.objects.filter(worker = Users.objects.get(id = request.session['id'])),
        'current_user' : Users.objects.get(id = request.session['id']),
        'jobs_empty' : Job.objects.filter(worker__isnull = True)
    }
    return render(request, 'helper/dashboard.html', user_data)
def add(request):
    hasErrors = Job.objects.job_val(request.POST)
    if len(hasErrors) > 0:
        for error in hasErrors:
            messages.error(request, hasErrors[error])
        return redirect('/helper/add_jobs_page')
    else:
        Job.objects.create(title=request.POST['title'],description=request.POST['description'], location=request.POST['location'], creator=Users.objects.get(id = request.session['id']))
        return redirect('/helper/load_dash')
def add_jobs_page(request):
    return render(request, 'helper/add.html')
def logout(request):
    request.session['id'] = None
    return redirect('/helper')
def view(request, job_id):
    job_dict = {
        'current_job': Job.objects.get(id=job_id)
    }
    return render(request, 'helper/show.html', job_dict)
def add_my_job(request, job_id):
    Job.objects.filter(id=job_id).update(worker=Users.objects.get(id=request.session['id']))
    return redirect('/helper/load_dash')
def edit_jobs_page(request, job_id):
    context = {
        'job' : Job.objects.get(id=job_id)
    }
    return render(request, 'helper/edit.html', context)
def edit(request, job_id):
    b = Job.objects.get(id=job_id)
    b.title=request.POST['title']
    b.description=request.POST['description']
    b.location=request.POST['location']
    b.save()
    return redirect('/helper/load_dash')
def delete(request, job_id):
    b = Job.objects.get(id=job_id) 
    b.delete()
    return redirect('/helper/load_dash')
