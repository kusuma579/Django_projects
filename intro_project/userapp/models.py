from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(max_length=55)

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(max_length=55)
    phone=models.IntegerField()
    history=models.TextField()
    designation=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)
    project=models.CharField(max_length=100)
    team_name=models.CharField(max_length=100)

