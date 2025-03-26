from django.shortcuts import reverse
from django.views.generic import TemplateView, CreateView
from django.core.paginator import Paginator

from core.models import Question
from core.forms import QuestionForm


class HomePage(TemplateView):
    template_name = "main.html"
    extra_context = {"title": 'Главная'}


class MaterialsPage(TemplateView):
    template_name = "materials.html"
    extra_context = {"title": 'Копилка'}


class QuestionsPage(CreateView):
    template_name = "questions.html"
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Консультирование'

        paginator = Paginator(Question.objects.filter(status=1), 4)
        page_number = self.request.GET.get("page", 1)
        questions = paginator.get_page(page_number)

        context['questions'] = questions

        return context

    def get_success_url(self):
        self.request.session['thanks_message'] = ("Спасибо за вопрос! Скоро ответ появится на сайте или с вами "
                                                  "свяжутся лично.")
        return reverse("thanks")


class ViewQuestion(TemplateView):
    template_name = "question.html"

    def get_context_data(self, question_id, **kwargs):
        context = super().get_context_data(**kwargs)
        question = Question.objects.get(id=question_id)
        context['title'] = question.title
        context['question'] = question
        return context


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Спасибо!'
        context['thanks_message'] = self.request.session.pop('thanks_message',
                                                             'Спасибо за посещение сайта!')
        return context

