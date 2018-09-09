from django.db import models

# Create your models here.
class Deportista(models.Model):
    KINDS = (
        ('A','Cédula de ciudadanía'),
        ('B','Cédula de extrangería'),
        ('C','Nit'),
    )
    SUBSCRIPTION_KINDS = (
        ('A','Free'),
        ('B','Champion'),
        ('C','Super Champion'),
    )
    BODIES_KINDS = (
        ('A','Endomorfo'),
        ('B','Mesomorfo'),
        ('C','Ectomorfo'),
    )
    doc_kind = models.CharField(max_length=1,choices=KINDS,default='A')
    doc = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    first_lastname = models.CharField(max_length=20)
    second_lastname = models.CharField(max_length=20)
    cellphone_number = models.CharField(max_length=20)
    interested_sports = models.ManyToManyField('sports.Sport')
    subscription_date = models.DateTimeField(auto_now_add=True)
    subscription_update_date = models.DateTimeField(auto_now = True)
    subscription_kind = models.CharField(max_length=1,choices=SUBSCRIPTION_KINDS,default='A')
    body = models.CharField(max_length=1,choices=BODIES_KINDS,default='A')
    height = models.DecimalField(max_digits=3,decimal_places=3)
    weight = models.DecimalField(max_digits=3,decimal_places=3)
    intereses = models.TextField(max_length=255)
    dirección = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name
