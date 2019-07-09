from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime


def index(request):
    return render(request, 'session_words/index.html')
def add_word(request):
    if request.method == 'POST':
        wordtime = strftime('%H: %M: %S%p, %D, %Y', localtime())
        if 'words' not in request.session:
            request.session['words'] = []
        if 'bigfont' in request.POST:
            data = {
                'word' : request.POST['word'],
                'color' : request.POST['color'],
                'font' : 'big',
                'time' : wordtime
            }
        else:
            data = {
                'word' : request.POST['word'],
                'color' : request.POST['color'],
                'font' : 'small',
                'time' : wordtime
            }
        request.session['words'].append(data)
    return redirect('/session_words/index')
    
def clear(request):
    request.session.clear()
    return redirect('/session_words/index')