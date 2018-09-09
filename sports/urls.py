from django.urls import path
from sports import views

app_name = 'sports'

urlpatterns = [
    path('',views.HomeSports,name='home'),
]
