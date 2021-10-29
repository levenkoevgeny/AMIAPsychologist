from django.forms import ModelForm
from .models import PersonalWork
from django import forms

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class PersonalWorkForm(ModelForm):
    class Meta:
        model = PersonalWork
        fields = ['lastname', 'work_date', 'rank', 'subdivision', 'work_kind', 'work_request', 'work_done',
                  'conclusion', 'recommendations', 'extra_data']
        widgets = {'work_date': myDateInput}
