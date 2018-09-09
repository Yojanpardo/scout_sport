from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.

class HomeClubs(TemplateView):
    template_name = 'clubs/home.html'
