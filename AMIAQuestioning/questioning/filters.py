import django_filters
from .models import Questionary
from django import forms


class QuestioningFilter(django_filters.FilterSet):
    time_added__year = django_filters.NumberFilter(field_name='time_added__year')

    class Meta:
        model = Questionary
        fields = ['time_added__year']