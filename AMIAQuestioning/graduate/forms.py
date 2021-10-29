from django.forms import ModelForm
from .models import *
from django import forms

NO_YES_CHILDREN = [
    ('0', 'Нет'),
    ('1', 'Да (пол и год рождения ребенка):'),
]

NO_YES = [
    ('0', 'Нет'),
    ('1', 'Да'),
]

DIVORCED_LIVE = [
    ('1', 'раздельно'),
    ('2', 'совместно'),
]

STEPFATHER_STEPMOTHER_MARRIAGE = [
    ('1', 'в браке'),
    ('2', 'без регистрации брака'),
]

MOTHER_FATHER_DATA = [
    ('1', 'матери'),
    ('2', 'отце'),
    ('3', 'обоих'),
]

LEVEL_OF_SPORT = [
    ('1', 'на любительском уровне'),
    ('2', 'профессионально'),
]

PERIOD_OF_SPORT = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', 'ежедневно'),
]

WOULD_ADVISE = [
    ('1', 'Да'),
    ('2', 'Нет'),
    ('3', 'Не знаю'),
]

NEED_CONVERSATION = [
    ('1', 'В беседе не нуждаюсь.'),
    ('2', 'Хотелось бы побеседовать (укажите, что конкретно Вы хотели бы обсудить)'),
]


class GraduatingForm(ModelForm):

    class Meta:

        model = GraduateForm

        exclude = ['fill_date_time']

        widgets = {
            'rank': forms.Select(choices=Rank.objects.all()),
            'position': forms.Select(choices=Position.objects.all()),
            'stepfather_stepmother_marriage_mother': forms.RadioSelect(choices=STEPFATHER_STEPMOTHER_MARRIAGE),
            'stepfather_stepmother_marriage_father': forms.RadioSelect(choices=STEPFATHER_STEPMOTHER_MARRIAGE),
            'divorced_live': forms.RadioSelect(choices=DIVORCED_LIVE),
            'has_children': forms.RadioSelect(choices=NO_YES_CHILDREN),
            'sport_is_only_by_program': forms.Select(choices=NO_YES),
            'sport_level': forms.RadioSelect(choices=LEVEL_OF_SPORT),
            'sport_period': forms.Select(choices=PERIOD_OF_SPORT),
            'is_satisfied_with_the_training': forms.RadioSelect(choices=SatisfiedWithTheTraining.objects.all()),
            'expectations': forms.RadioSelect(choices=Expectations.objects.all()),
            'character_change': forms.RadioSelect(choices=CharacterChange.objects.all()),
            'would_advise': forms.RadioSelect(choices=WOULD_ADVISE),
            'after_graduating': forms.RadioSelect(choices=AfterGraduating.objects.all()),
            'need_conversation': forms.RadioSelect(choices=NEED_CONVERSATION),
            'mother_father_data': forms.RadioSelect(choices=MOTHER_FATHER_DATA),
            'guardians': forms.CheckboxSelectMultiple(choices=Guardian.objects.all()),

            'what_induce_to_quit': forms.CheckboxSelectMultiple(choices=WhatInduceToQuit.objects.all()),
            'what_keeps': forms.CheckboxSelectMultiple(choices=WhatKeeps.objects.all()),
            'how_did_teachers_influence': forms.RadioSelect(choices=HowDidTeachersInfluence.objects.all()),
            'how_did_leaders_influence': forms.RadioSelect(choices=HowDidLeadersInfluence.objects.all()),
            'i_inform': forms.CheckboxSelectMultiple(choices=Inform.objects.all()),
        }