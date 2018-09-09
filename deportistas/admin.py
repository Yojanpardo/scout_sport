from django.contrib import admin
from .models import Deportista
# Register your models here.
@admin.register(Deportista)
class AdminDeportista(admin.ModelAdmin):
    list_display=('first_name','interested_sport',)
