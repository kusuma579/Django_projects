from django.db import models

# Create your models here.
class Traveler(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    destination = models.CharField(max_length=100)
    budget = models.IntegerField()

    mood = models.CharField(max_length=50)

    def __str__(self):
        return self.name