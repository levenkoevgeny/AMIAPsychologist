import django_filters
from .models import Anketa
from django import forms


class CourseFilter(django_filters.FilterSet):

    PROVIDED_CHOICES = (
        (2, 'Да'),
        (1, 'Нет'),
    )

    military = django_filters.ChoiceFilter(choices=PROVIDED_CHOICES, widget=forms.Select)
    fio = django_filters.CharFilter(lookup_expr='icontains')
    index_number = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Anketa
        fields = ['group']