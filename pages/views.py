from django.shortcuts import render
from .models import Trainee, Report, Reportweek
from .scrapper import badgefetcher
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

def badges(request):
    name = request.GET['name']
    
    trainee = Trainee.objects.filter(name=name).values('credly')
    
    url = trainee[0]['credly']
    
    badges = badgefetcher(url)

    context = {
        'badges': badges
    }
    return render(request, 'cohort.html', context)

@csrf_exempt
def students(request):
    if request.method == "POST":
        name = request.POST['name']
        cohort = request.POST['cohort']
        week = request.POST['week']
        results = request.POST['results']
        challenges = request.POST['challenges']
        plans = request.POST['plans']
        new_report = Report(name=name, cohort=cohort, report_week=week, results=results, challenges=challenges, plan=plans)
        new_report.save()
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

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        cohort = request.POST['cohort']
        credly = request.POST['credly']

        new_trainee = Trainee(name=name, cohort=cohort, credly=credly)
        new_trainee.save()

    return render(request, 'registration.html')

@csrf_exempt
def reports(request):
    if request.method == 'POST':
        week = request.POST['week']

        new_week = Reportweek(report_week=week)
        print(new_week)
        new_week.save()
    current_week = Reportweek.objects.all().last()
    
    reports = Report.objects.filter(report_week=current_week)

    context = {
        'week': current_week,
        'reports': reports
    }
    return render(request, 'reports.html', context)

def resources(request):
    return render(request, 'resources.html')

def help(request):
    return render(request, 'help.html')