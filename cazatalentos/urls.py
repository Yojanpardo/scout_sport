from django.urls import path
from cazatalentos import views

app_name = 'cazatalentos'

urlpatterns = [
    path('',views.HomeCazatalentos.as_view(),name='home'),
    path('register/',views.RegisterCazatalento.as_view(),name='register'),
]
