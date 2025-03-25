from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from core.models import Question


class HomePage(TemplateView):
    template_name = "main.html"
    extra_context = {"title": 'Главная'}


class MaterialsPage(TemplateView):
    template_name = "materials.html"
    extra_context = {"title": 'Копилка'}


class QuestionsPage(TemplateView):
    template_name = "questions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Консультирование'

        paginator = Paginator(Question.objects.filter(status=1), 4)
        page_number = self.request.GET.get("page", 1)
        questions = paginator.get_page(page_number)

        context['questions'] = questions

        return context


class ViewQuestion(TemplateView):
    template_name = "question.html"

    def get_context_data(self, question_id, **kwargs):
        context = super().get_context_data(**kwargs)
        question = Question.objects.get(id=question_id)
        context['title'] = question.name
        context['question'] = question
        return context
