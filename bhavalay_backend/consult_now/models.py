# models.py

from django.db import models

class Consultation(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    occupation = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    otp = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.name