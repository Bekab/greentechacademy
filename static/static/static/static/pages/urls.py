from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cohort', views.cohort, name='cohort'),
    path('students', views.students, name='students'),
    path('profiles', views.profiles, name='profiles'),
    path('registration', views.registration, name='registration'),
    path('reports', views.reports, name='reports'),
]