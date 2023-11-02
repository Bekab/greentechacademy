from django.shortcuts import render
from .models import Trainee, Report, Reportweek, Resource, Ticket
from .scrapper import badgefetcher
from django.views.decorators.csrf import csrf_exempt

def landingpage(request):
    return render(request, 'landingpage.html')

def index(request):
    a = int(Trainee.objects.filter(cohort='cohort a').count())
    b = int(Trainee.objects.filter(cohort='cohort b').count())
    c = int(Trainee.objects.filter(cohort='cohort c').count())
    d = int(Trainee.objects.filter(cohort='cohort d').count())
    cohorts = ['Cohort A', 'Cohort B', 'Cohort C', 'Cohort D']
    counts = [a, b, c, d]

    context = {
        'cohorts': cohorts,
        'counts': counts
    }

    return render(request, 'index.html', context)

def badges(request):
    name = request.GET['name']
    
    trainee = Trainee.objects.filter(name=name).values('credly')
    
    if not trainee:
        context = {
            'name': name
        }
        return render(request, 'badgeserror.html', context)
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

@csrf_exempt
def profiles(request):
    trainees = Trainee.objects.all()

    context = {
        'trainees': trainees
    }

    return render(request, 'profiles.html', context)

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        if 'credly' in request.POST.keys():
            name = request.POST['name']
            cohort = request.POST['cohort']
            credly = request.POST['credly']

            new_trainee = Trainee(name=name, cohort=cohort, credly=credly)
            new_trainee.save()
        
        if 'link' in request.POST.keys():
            name = request.POST['name']
            link = request.POST['link']
            description = request.POST['description']

            new_resource = Resource(name=name, link=link, description=description)
            new_resource.save()
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
    resources = Resource.objects.all()

    context = {
        'resources': resources
    }
    return render(request, 'resources.html', context)

@csrf_exempt
def help(request):
    if request.method == "POST":
        name = request.POST['name']
        question = request.POST['question']
        solved = False

        new_ticket = Ticket(name=name, question=question, solved=solved)
        new_ticket.save()

    return render(request, 'help.html')

def tickets(request):

    tickets = Ticket.objects.all()
    
    context = {
        'tickets': tickets
    } 
    return render(request, 'tickets.html', context)