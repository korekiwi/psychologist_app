from django.shortcuts import reverse
from django.views.generic import TemplateView, CreateView
from django.core.paginator import Paginator
from django.db.models import Q, F

from core.models import Question, Document
from core.forms import QuestionForm, AppointmentForm


class HomePage(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Детский психолог Шикуля Н.А.'
        context['documents'] = Document.objects.all()
        return context


class QuestionsPage(CreateView):
    template_name = "questions.html"
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Консультирование'

        questions_objects = Question.objects.filter(status=1)

        search_query = self.request.GET.get("search_query", "")
        print(search_query)

        if search_query:
            q_object = Q()
            q_object |= Q(title__icontains=search_query)
            q_object |= Q(question__icontains=search_query)
            questions_objects = questions_objects.filter(q_object).distinct()

        sort_by = self.request.GET.get("sort_by", "views")

        if sort_by == "views":
            questions_objects = questions_objects.order_by('-views')
        elif sort_by == "created_at":
            questions_objects = questions_objects.order_by('-created_at')

        paginator = Paginator(questions_objects, 4)
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

        session = self.request.session
        key = f"viewed_posts_{question.id}"

        if key not in session:
            Question.objects.filter(id=question_id).update(views=F("views") + 1)
            session[key] = True
            question.refresh_from_db()

        context['title'] = question.title
        context['question'] = question

        return context


class AppointmentPage(CreateView):
    template_name = "appointment.html"
    form_class = AppointmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запись на прием'
        return context

    def get_success_url(self):
        self.request.session['thanks_message'] = "Ваша запись была одобрена. Скоро я свяжусь с Вами лично."
        return reverse("thanks")


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Спасибо!'
        context['thanks_message'] = self.request.session.pop('thanks_message',
                                                             'Спасибо за посещение сайта!')
        return context

