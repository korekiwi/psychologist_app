from django.db import models


class Question(models.Model):
    STATUS_CHOICES = [
        (0, 'Не рассмотрен'),
        (1, 'Подтвержден'),
        (2, 'Отклонен'),
    ]

    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон", null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name="Email", null=True, blank=True)
    telegram = models.CharField(max_length=50, verbose_name="Телеграм", null=True, blank=True)
    question = models.TextField(verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='Статус')
    answer = models.TextField(null=True, blank=True, verbose_name="Ответ")

    def __str__(self):
        return f'{self.name} - {self.question}'

    def save(self, *args, **kwargs):
        if self.pk:
            if self.status == self.STATUS_CHOICES[1][0] and not self.answer:
                self.status = self.STATUS_CHOICES[0][0]
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


# class Answer(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     text = models.TextField(verbose_name='Текст ответа')
#     question = models.OneToOneField(Question, on_delete=models.CASCADE, primary_key=True)
#
#     def __str__(self):
#         return f'{self.question}'
#
#     class Meta:
#         verbose_name = "Ответ"
#         verbose_name_plural = "Ответы"
