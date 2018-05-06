from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if request.method == 'GET':
        return render(request, 'survey_project/index.html')

def process(request):
    if request.method == 'POST':
        if not 'tries' in request.session:
            request.session['tries'] = 0
        request.session['tries'] += 1
        request.session['context'] = { 'name': request.POST.get('name'), 'location': request.POST.get('location'), 'language': request.POST.get('language'), 'comments': request.POST.get('comments') }
        return redirect('/result')

def result(request):
    if request.method == 'GET':
        return render(request, 'survey_project/results.html', request.session.pop('context'))
