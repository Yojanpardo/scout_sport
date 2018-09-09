from django.urls import path
from cazatalentos import views

app_name = 'cazatalentos'

urlpatterns = [
    path('',views.HomeCazatalentos,name='home'),
]
