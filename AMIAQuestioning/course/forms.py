from django.forms import ModelForm
from .models import *
from django import forms


myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class AnketaForm(ModelForm):

    class Meta:
        PERIODICITY = [
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', 'Ежедневно'),
        ]

        LEVEL_OF_WEALTH = [
            ('1', 'высокая'),
            ('2', 'выше средней'),
            ('3', 'средняя'),
            ('4', 'ниже средней'),
            ('5', 'низкая'),
        ]

        ROOM_COUNT = [
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5 и более'),
        ]

        PEOPLE_COUNT = [
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5 и более'),
        ]

        OWN_ROOM = [
            ('1', 'Да'),
            ('2', 'Нет'),
        ]

        NO_YES = [
            ('1', 'Нет'),
            ('2', 'Да (укажите какие)'),
        ]

        NO_YES_CHILDREN = [
            ('1', 'Нет'),
            ('2', 'Да (укажите пол и год рождения)'),
        ]

        PREMISES = [
            ('1', 'Квартира'),
            ('2', 'Частный дом'),
            ('3', 'Комната (блок) в общежитии'),
            ('4', 'Иное'),
        ]

        FAMILY_STATUSES = [
            ('1', 'Холост'),
            ('2', 'Не замужем'),
            ('3', 'Женат'),
            ('4', 'Замужем'),
            ('5', 'Разведен(а)'),
            ('6', 'Вдовец'),
            ('7', 'Вдова'),
        ]

        model = Anketa

        fields = [
            'group', 'fio', 'index_number', 'nationality', 'religion', 'date_of_birth', 'birth_place',
            'year_of_graduation', 'specialty',
            'military_year_since', 'military_year_till', 'military_place', 'type_of_army',
            'marriage_year_since', 'marriage_year_till',
            'family_status', 'children', 'children_info',
            'participation_in_education', 'participation_in_education_other',
            'parents_not_in_marriage_since',
            'mother_only_father_died_year', 'mother_only_other', 'father_only_mother_died_year', 'father_only_other', 'relationship', 'relationship_other',
            'siblings',
            'interest', 'interest_other',
            'kind_of_sport', 'periodicity', 'achievements', 'not_prof',
            'guardian', 'guardian_other', 'is_chronic_diseases', 'chronic_diseases', 'is_injury', 'injury',
            'particular_qualities', 'particular_qualities_other',
            'relatives_record', 'relatives_record_other',
            'level_of_wealth',
            'living_conditions_premises_other',
            'living_conditions_room_count',
            'living_conditions_people_count',
            'is_own_room',
            'living_conditions_premises',
            'activity', 'activity_other',
            'ability', 'ability_other',
            'gaming_hours', 'friends_count',
            'messenger', 'messenger_other',
            'smoking_try_in_year', 'smoking_beginning_in_year', 'smoking_ending_in_year',
            'if_had_not_entered'
        ]

        required = (
            'participation_in_education',
        )
        widgets = {'date_of_birth': myDateInput,
                   'guardian': forms.CheckboxSelectMultiple(choices=Guardian.objects.all()),
                   'periodicity': forms.Select(choices=PERIODICITY),
                   'level_of_wealth': forms.RadioSelect(choices=LEVEL_OF_WEALTH),
                   'living_conditions_room_count': forms.RadioSelect(choices=ROOM_COUNT),
                   'living_conditions_people_count': forms.RadioSelect(choices=PEOPLE_COUNT),
                   'is_own_room': forms.RadioSelect(choices=OWN_ROOM),
                   'living_conditions_premises': forms.RadioSelect(choices=PREMISES),
                   'activity': forms.CheckboxSelectMultiple(choices=Activity.objects.all()),
                   'ability': forms.CheckboxSelectMultiple(choices=Ability.objects.all()),
                   'messenger': forms.CheckboxSelectMultiple(choices=Messenger.objects.all()),
                   'particular_qualities': forms.CheckboxSelectMultiple(choices=ParticularQualities.objects.all()),
                   'relatives_record': forms.CheckboxSelectMultiple(choices=RelativesRecord.objects.all()),
                   'participation_in_education': forms.CheckboxSelectMultiple(choices=ParticipationInEducation.objects.all()),
                   'is_injury': forms.RadioSelect(choices=NO_YES),
                   'is_chronic_diseases': forms.RadioSelect(choices=NO_YES),
                   'family_status': forms.RadioSelect(choices=FAMILY_STATUSES),
                   'children': forms.RadioSelect(choices=NO_YES_CHILDREN),
                   'relationship': forms.CheckboxSelectMultiple(choices=Relationship.objects.all()),
                   'interest': forms.CheckboxSelectMultiple(choices=Interest.objects.all()),
                   }
