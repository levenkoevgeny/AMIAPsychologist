from django.forms import ModelForm
from .models import *
from django import forms


class QuestionaryForm(ModelForm):

    class Meta:

        SEX_CHOICES = [('1', 'Мужской'), ('2', 'Женский')]
        LAW_CHOICES = [('1', 'Да'), ('0', 'Нет')]

        model = Questionary
        fields = '__all__'

        widgets = {'sex': forms.RadioSelect(choices=SEX_CHOICES),
                   'in_the_interests_of': forms.RadioSelect(choices=Interest.objects.all()),
                   'graduate': forms.RadioSelect(choices=Educational.objects.all()),
                   'is_law_orientation': forms.RadioSelect(choices=LAW_CHOICES),
                   'place_of_last_education': forms.RadioSelect(choices=EducationalPlace.objects.all()),
                   'live_region': forms.RadioSelect(choices=LivePlaceRegion.objects.all()),
                   'attend_extra': forms.CheckboxSelectMultiple(choices=AttendExtra.objects.all()),
                   'important_for': forms.CheckboxSelectMultiple(choices=ImportantFor.objects.all()),
                   'important_for_spec': forms.CheckboxSelectMultiple(choices=ImportantForSpec.objects.all()),
                   'got_information_from': forms.CheckboxSelectMultiple(choices=GotInformationFrom.objects.all()),
                   'decision': forms.RadioSelect(choices=Decision.objects.all()),
                   'let_you': forms.CheckboxSelectMultiple(choices=LetYou.objects.all()),
                   'difficulty': forms.RadioSelect(choices=Difficulty.objects.all()),
                   'get_education': forms.RadioSelect(choices=GetEducation.objects.all()),
                   }



