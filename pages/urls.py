from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('index', views.index, name='index'),
    path('badges', views.badges, name='badges'),
    path('students', views.students, name='students'),
    path('profiles', views.profiles, name='profiles'),
    path('registration', views.registration, name='registration'),
    path('reports', views.reports, name='reports'),
    path('resources', views.resources, name='resources'),
    path('help', views.help, name='help'),
    path('tickets', views.tickets, name='tickets'),

]