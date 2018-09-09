from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

# Create your views here.

class HomeSports(TemplateView):
    template_name = 'Sports/home.html'
