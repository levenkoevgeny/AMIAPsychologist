from django.contrib import admin
from .models import *


admin.site.register(BekaScale)
admin.site.register(Result)
# admin.site.register(Position)


@admin.register(Question)
class QuestionPageAdmin(admin.ModelAdmin):
    list_display = ('question_number', 'question_text')
    list_display_links = ('question_text',)
    search_fields = ['question_text']
    list_filter = ('question_text',)
