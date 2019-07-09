from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from .models import User

# Create your views here.
def index(request):
    for object in User.objects.all():
        context = {
            'id': object.id,
            'first_name': object.first_name,
            'last_name': object.last_name,
            'email': object.email,
            'created_at': object.created_at,
        }
    context = {
        'user_data': User.objects.all(),
    }
    return render(request, 'users/index.html', context)
def create_user(request):
    return render(request, 'users/new.html')
def create(request):
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect('/users/')
def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'users/show.html', context)
def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'users/edit.html', context)
def update(request, user_id):
    b = User.objects.get(id=user_id)
    b.first_name=request.POST['first_name']
    b.last_name=request.POST['last_name']
    b.email=request.POST['email']
    b.updated_at = datetime.now()
    b.save()
    return redirect('/users/'+user_id)
def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users/')