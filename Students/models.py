from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField()

class RankSheet(models.Model):
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social_science = models.IntegerField()
    total = models.IntegerField()
    average = models.FloatField()
    result = models.BooleanField()
