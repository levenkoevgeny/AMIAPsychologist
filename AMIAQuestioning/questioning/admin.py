from django.contrib import admin
from .models import *


# admin.site.register(Interest)
# admin.site.register(Educational)
# admin.site.register(EducationalPlace)
# admin.site.register(LivePlaceRegion)
# admin.site.register(AttendExtra)
# admin.site.register(ImportantFor)
# admin.site.register(ImportantForSpec)
# admin.site.register(GotInformationFrom)
# admin.site.register(Decision)
# admin.site.register(LetYou)
# admin.site.register(Difficulty)
# admin.site.register(GetEducation)

# admin.site.register(Questionary)
#
#
@admin.register(Questionary)
class QuestionaryPageAdmin(admin.ModelAdmin):
    list_display = (
        'time_added', 'in_the_interests_of_other', 'important_for_other', 'got_information_from_other', 'decision_other')
    list_display_links = ('time_added',)
    list_filter = ('time_added', 'in_the_interests_of_other', 'important_for_other', 'got_information_from_other', 'decision_other')
    search_fields = ['time_added', 'in_the_interests_of_other']
    filter_horizontal = ('attend_extra', 'important_for', 'important_for_spec', 'got_information_from', 'let_you',)


    # l = Questionary.objects.filter(time_added__month=)