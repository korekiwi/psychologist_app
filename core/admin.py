from django.contrib import admin

from core.models import Question


def make_accepted(modeladmin, request, queryset):
    updated = queryset.update(status=1)


def make_declined(modeladmin, request, queryset):
    updated = queryset.update(status=2)


def make_unverified(modeladmin, request, queryset):
    updated = queryset.update(status=0)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "question", "answer")
    search_fields = ("name", "status")
    list_editable = ("status", "answer")
    list_filter = ("name", "status", "phone", "email")

    make_accepted.short_description = 'Одобрить выбранные записи'
    make_declined.short_description = 'Отклонить выбранные записи'
    make_unverified.short_description = 'Отметить неподтвержденными'

    actions = [make_accepted, make_declined, make_unverified]

# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ("question", "text")
#     search_fields = ("question", "text")
#     list_filter = ("question",)

# Register your models here.
