from django.urls import path
from clubs import views, RegisterClub

app_name = 'clubs'

urlpatterns = [
    path('',views.HomeClubs,name='home'),
    path('register/',views.RegisterClub.as_view(),name='register'),
    path('previsualizacion_jugadores',views.PrevisualizacionJugadores.as_view(),name='previsualizacion juagadores')
]
