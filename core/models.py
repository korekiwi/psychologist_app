from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Question(models.Model):
    STATUS_CHOICES = [
        (0, 'Не рассмотрен'),
        (1, 'Подтвержден'),
        (2, 'Отклонен'),
    ]

    title = models.CharField(max_length=100, verbose_name='Проблема')
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон", null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name="Email", null=True, blank=True)
    telegram = models.CharField(max_length=50, verbose_name="Телеграм", null=True, blank=True)
    question = models.TextField(verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='Статус')
    answer = models.TextField(null=True, blank=True, verbose_name="Ответ")
    views = models.IntegerField(blank=True, default=0,  verbose_name='Просмотры')

    def __str__(self):
        return f'{self.name} - {self.question}'

    def get_absolute_url(self):
        return reverse("question", args=[self.pk])

    def save(self, *args, **kwargs):
        if self.pk:
            if self.status == self.STATUS_CHOICES[1][0] and not self.answer:
                self.status = self.STATUS_CHOICES[0][0]
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Appointment(models.Model):
    STATUS_CHOICES = [
        (0, 'Не рассмотрена'),
        (1, 'Подтверждена'),
        (2, 'Отклонена'),
    ]

    title = models.CharField(max_length=100, verbose_name='Проблема')
    adult_name = models.CharField(max_length=100, verbose_name="Имя")
    child_name = models.CharField(max_length=100, verbose_name="Имя ребенка")
    child_age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(18)],
                                    verbose_name='Возраст ребенка')
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.CharField(max_length=50, verbose_name="Email", null=True, blank=True)
    telegram = models.CharField(max_length=50, verbose_name="Телеграм", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='Статус')
    problem = models.TextField(verbose_name='Описание проблемы')

    def __str__(self):
        return f'{self.adult_name} - {self.problem}'

    class Meta:
        verbose_name = "Запись на прием"
        verbose_name_plural = "Записи на прием"


class Document(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    image = models.ImageField(upload_to='education/', blank=True, null=True, verbose_name='Фотография')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
