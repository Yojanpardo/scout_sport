from django.db import models

# Create your models here.

class Scout(models.Model):
    KINDS=(
        ('A','Cédula de ciudadanía'),
        ('B','Cédula de extrangería'),
        ('C','Nit'),
    )
    doc_kind = models.CharField(max_length=1,choices=KINDS,default='A')
    doc = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    first_lastname = models.CharField(max_length=20)
    second_lastname = models.CharField(max_length=20)
    cellphone_number = models.CharField(max_length=20)
    interested_sports = models.ManyToManyField('sports.Sport')
