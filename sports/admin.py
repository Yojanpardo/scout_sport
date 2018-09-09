from django.contrib import admin
from .models import Sport

# Register your models here.
@admin.register(Sport)
class AdminSport(admin.ModelAdmin):
    list_display=('name',)
