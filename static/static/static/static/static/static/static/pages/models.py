from django.db import models

# Create your models here.

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=50)
    credly = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Report(models.Model): 
    name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=50)
    report_week = models.CharField(max_length=50)
    results = models.CharField(max_length=500)
    challenges = models.CharField(max_length=500)
    plan = models.CharField(max_length=500)

    def __str__(self):
        return "{} - {}".format(self.name, self.report_week)

class Reportweek(models.Model):
    report_week = models.CharField(max_length=50)

    def __str__(self):
        return self.report_week
    
class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=300)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

