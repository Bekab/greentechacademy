from django.shortcuts import render
from .models import Trainee, Report, Reportweek
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
    week = Reportweek.objects.all().last()
    context = {
        'week': week
    }
    return render(request, 'students.html', context)

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
    if request.method == 'POST':
        week = request.POST['week']

        new_week = Reportweek(report_week=week)
        print(new_week)
        new_week.save()
    current_week = Reportweek.objects.all().last()
    print(current_week.report_week)
    context = {
        'week': current_week
    }
    return render(request, 'reports.html', context)