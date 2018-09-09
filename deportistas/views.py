from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

# Create your views here.

class HomeDeportistas(TemplateView):
    template_name = 'deportistas/home.html'
