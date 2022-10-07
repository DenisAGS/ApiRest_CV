from django.db import models

# Create your models here.
class Datos(models.Model):
    work_experience= models.TextField(blank=True)
    education= models.TextField(blank=True)
    interests=models.TextField(blank=True)
    languajes=models.TextField(blank=True)
    certificates=models.TextField(blank=True)
    skills=models.TextField(blank=True)