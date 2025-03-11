from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "main.html"
    extra_context = {"title": 'Главная'}

class MaterialsPage(TemplateView):
    template_name = "materials.html"
    extra_context = {"title": 'Копилка'}

class QuestionsPage(TemplateView):
    template_name = "questions.html"
    extra_context = {"title": 'Консультирование'}

