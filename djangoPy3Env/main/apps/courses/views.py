from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
import re
from .models import Course


def index(request):
        data = {
            'course_data' : Course.objects.all()
        }
        return render(request, 'courses/index.html', data)
def add(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/courses')
def remove(request, course_id):
    course_dict = {
        'current_course': Course.objects.get(id=course_id)
    }
    return render(request, 'courses/delete.html', course_dict)
def delete(request, course_id):
    b = Course.objects.get(id=course_id) 
    b.delete()
    return redirect('/courses')