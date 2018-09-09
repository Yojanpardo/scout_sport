from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

# Create your views here.

class HomeCazatalentos(TemplateView):
    template_name = 'cazatalentos/home.html'
