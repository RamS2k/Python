from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    unique_id = get_random_string(length=14)
    context = {
        "counter" : request.session['count'],
        "word" : unique_id
    }
    return render(request, 'random_word/index.html', context)
def attempt(request):
    request.session['count'] += 1
    return redirect('/random_word/index')
def reset(request):
    request.session['count'] = 0
    return redirect('/random_word/index')