from django.db import models

# Create your models here.

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=50)
    credly = models.CharField(max_length=300)

class Report(models.Model):
    report_week = models.CharField(max_length=50) 
    name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=50)
    results = models.CharField(max_length=500)
    challanges = models.CharField(max_length=500)
    plan = models.CharField(max_length=500)

