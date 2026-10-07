from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(default=0)

    def __str__(self):
       return self.name

class Task(models.Model):

    student_reference = models.ForeignKey(Student,null=True,on_delete=models.CASCADE)
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
