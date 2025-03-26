from django import forms
from django.core.validators import EmailValidator
import re

from core.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "name", "phone", "email", "telegram", "question"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Краткое описание проблемы"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ваше имя"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Телефон"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "telegram": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Телеграм"}
            ),
            "question": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Вопрос"}
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise forms.ValidationError("Поле должно содержать минимум 2 символа.")
        elif len(title) > 100:
            raise forms.ValidationError("Поле не должно содержать более 100 символов.")
        return title

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Имя должно содержать минимум 2 символа.")
        elif len(name) > 100:
            raise forms.ValidationError("Имя не должно содержать более 100 символов.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        reg = "^\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
        if phone and re.fullmatch(reg, phone) is None:
            raise forms.ValidationError("Номер телефона введен неверно.")
        return phone

    def clean_email(self):
        reg = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
        email = self.cleaned_data.get('email')
        if email and re.fullmatch(reg, email) is None:
            raise forms.ValidationError("Email введен неверно.")
        return email

    def clean_telegram(self):
        reg = "(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)"
        telegram = self.cleaned_data.get('telegram')
        if telegram and re.fullmatch(reg, telegram) is None:
            raise forms.ValidationError("Telegram введен неверно.")
        return telegram

    def clean_question(self):
        question = self.cleaned_data.get("question")
        if len(question) < 30:
            raise forms.ValidationError("Вопрос должен содержать не менее 30 символов.")
        return question


