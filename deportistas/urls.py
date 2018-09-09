from django.urls import path
from deportistas import views

app_name = 'deportistas'

urlpatterns = [
    path('',views.HomeDeportistas,name='home'),
    path('register/',views.Registerde.as_view(),name='register'),
]
