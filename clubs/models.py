from django.db import models

# Create your models here.

class Club(models.Model):
    KINDS=(
        ('A','Nit'),
    )
    SUBSCRIPTION_KINDS = (
        ('A','Free'),
        ('B','Premium'),
    )
    doc_kind = models.CharField(max_length=1,choices=KINDS,default='A')
    doc = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    cellphone_number = models.CharField(max_length=20)
    interested_sports = models.ManyToManyField('sports.Sport')
    subscription_kind = models.CharField(max_length=1,choices=SUBSCRIPTION_KINDS,default='A')
    subscription_date = models.DateTimeField(auto_now_add=True)
    subscription_update_date = models.DateTimeField(auto_now = True)
