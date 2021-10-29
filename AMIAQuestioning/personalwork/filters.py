import django_filters
from django import forms
from django.contrib.auth.models import User

from .models import PersonalWork, Subdivision, Rank, WorkKind, WorkDone, Request


class PersonalWorkFilter(django_filters.FilterSet):
    lastname = django_filters.CharFilter(lookup_expr='icontains')
    work_date_start = django_filters.DateFilter(field_name='work_date', lookup_expr='gte',
                                                widget=forms.DateInput(
                                                    attrs={
                                                        'type': 'date'
                                                    }
                                                ))
    work_date_end = django_filters.DateFilter(field_name='work_date', lookup_expr='lte',
                                              widget=forms.DateInput(
                                                  attrs={
                                                      'type': 'date'
                                                  }
                                              ))
    subdivision = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    rank = django_filters.ModelMultipleChoiceFilter(queryset=Rank.objects.all())
    work_kind = django_filters.ModelMultipleChoiceFilter(queryset=WorkKind.objects.all())
    work_request = django_filters.ModelMultipleChoiceFilter(queryset=Request.objects.all())
    work_done = django_filters.ModelMultipleChoiceFilter(queryset=WorkDone.objects.all())
    executor = django_filters.ModelMultipleChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = PersonalWork
        fields = '__all__'
