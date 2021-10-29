from django.contrib import admin
from .models import *


admin.site.register(Group)
# admin.site.register(TestKind)
# admin.site.register(Interest)
# admin.site.register(ParticipationInEducation)
# admin.site.register(Relationship)
# admin.site.register(ParticularQualities)
# admin.site.register(RelativesRecord)
# admin.site.register(Activity)
# admin.site.register(Ability)
# admin.site.register(Messenger)
# admin.site.register(Guardian)
# admin.site.register(MotherFather)
# admin.site.register(StepmotherStepfather)
# admin.site.register(Anketa)


@admin.register(Anketa)
class AnketaPageAdmin(admin.ModelAdmin):
    list_display = (
        'group', 'fio')
    list_display_links = ('group',)
    list_filter = ('group',)
    search_fields = ['group', 'fio']
    filter_horizontal = ('participation_in_education', 'guardian', 'relationship', 'interest',
                         'particular_qualities', 'relatives_record', 'activity', 'ability', 'messenger')