from django.contrib import admin
from .models import Club
# Register your models here.
@admin.register(Club)
class AdminClub(admin.ModelAdmin):
    list_displa=('name','subscription_kind','subscription_date',)
