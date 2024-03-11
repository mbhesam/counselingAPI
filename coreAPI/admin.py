from django.contrib import admin
from coreAPI.models import Answers, Questions

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    pass

