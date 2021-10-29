from django.contrib import admin
from .models import *


# admin.site.register(Question)
admin.site.register(Questionary)
admin.site.register(Result)
admin.site.register(TestKind)


@admin.register(Question)
class QuestionPageAdmin(admin.ModelAdmin):
    list_display = ('question_number', 'question_text')
    list_display_links = ('question_text',)
    # filter_horizontal = ('question_text',)
    search_fields = ['question_text']
    list_filter = ('question_text',)
    # list_editable = ['question_number']
