from django.contrib import admin

from core.models import Question, Appointment


def make_accepted(modeladmin, request, queryset):
    updated = queryset.update(status=1)


def make_declined(modeladmin, request, queryset):
    updated = queryset.update(status=2)


def make_unverified(modeladmin, request, queryset):
    updated = queryset.update(status=0)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "name", "status", "question", "answer")
    search_fields = ("title", "name", "question")
    list_editable = ("status", "answer")
    list_filter = ("name", "status", "phone", "email")

    make_accepted.short_description = 'Одобрить выбранные записи'
    make_declined.short_description = 'Отклонить выбранные записи'
    make_unverified.short_description = 'Отметить неподтвержденными'

    actions = [make_accepted, make_declined, make_unverified]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("title", "adult_name", "child_name", "child_age", "status", "phone", "problem")
    search_fields = ("title", "adult_name", "child_name")
    list_editable = ("status",)
    list_filter = ("adult_name", "child_name", "status", "phone", "email")

    make_accepted.short_description = 'Подтвердить выбранные записи'
    make_declined.short_description = 'Отклонить выбранные записи'
    make_unverified.short_description = 'Отметить неподтвержденными'

    actions = [make_accepted, make_declined, make_unverified]

