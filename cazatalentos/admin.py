from django.contrib import admin
from .models import Scout

# Register your models here.

@admin.register(Scout)
class AdminScout(admin.ModelAdmin):
    list_display=('first_name','subscription_kind',)
