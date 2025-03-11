from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "main.html"