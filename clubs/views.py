from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.

class HomeClubs(TemplateView):
    template_name = 'clubs/home.html'

class PrevisualizacionJugadores(TemplateView):
    template_name = 'clubs/previsualizacion_jugadores.html'

class RegisterClub(TemplateView):
    template_name = 'clubs/register.html'
