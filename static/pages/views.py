from django.shortcuts import render
from .models import Trainee, Report
from .scrapper import badgefetcher


def index(request):
    return render(request, 'index.html')

def cohort(request):
    name = request.GET['name']
    
    trainee = Trainee.objects.filter(name=name).values('credly')
    
    url = trainee[0]['credly']
    
    badges = badgefetcher(url)

    context = {
        'badges': badges
    }
    return render(request, 'cohort.html', context)

def students(request):
    return render(request, 'students.html')

def profiles(request):
    trainees = Trainee.objects.all()

    context = {
        'trainees': trainees
    }

    return render(request, 'profiles.html', context)

def registration(request):

    if request.method == 'POST':
        name = request.POST['name']
        cohort = request.POST['cohort']
        credly = request.POST['credly']

        new_trainee = Trainee(name=name, cohort=cohort, credly=credly)
        new_trainee.save()

    return render(request, 'registration.html')

def reports(request):
    return render(request, 'reports.html')