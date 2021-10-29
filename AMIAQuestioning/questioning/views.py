from django.shortcuts import render
from .forms import QuestionaryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.utils import timezone
from django.views.decorators.cache import cache_page
from .filters import QuestioningFilter


# @cache_page(60 * 15)
def questioning_add(request):
    if request.method == 'POST':
        form = QuestionaryForm(request.POST)
        if form.is_valid():
            questioning = form.save()
            questioning.time_added = timezone.now()
            questioning.save()
            return HttpResponseRedirect(reverse('questioning:success'))
        else:
            return render(request, 'questioning/questioning_input_form.html', {'form': form})
    else:
        form = QuestionaryForm
        return render(request, 'questioning/questioning_input_form.html', {'form': form})


def success(request):
    return render(request, 'questioning/success.html')


def dashboard_pre_view(request):
    qs_set = {item.year_time_added for item in Questionary.objects.all()}
    return render(request, 'questioning/dashboard_pre_view.html', {
        'qs_set': qs_set,
    })


def dashboard(request):
    f = QuestioningFilter(request.GET, queryset=Questionary.objects.all())
    return render(request, 'questioning/dashboard.html', {'questioning_list': f.qs,
                                                          'interest_list': Interest.objects.all(),
                                                          'educational_list': Educational.objects.all(),
                                                          'educational_place_list': EducationalPlace.objects.all(),
                                                          'live_region_list': LivePlaceRegion.objects.all(),
                                                          'attend_extra_list': AttendExtra.objects.all(),
                                                          'important_for_list': ImportantFor.objects.all(),
                                                          'important_for_spec_list': ImportantForSpec.objects.all(),
                                                          'got_information_from_list': GotInformationFrom.objects.all(),
                                                          'decision_list': Decision.objects.all(),
                                                          'let_you_list': LetYou.objects.all(),
                                                          'difficulty_list': Difficulty.objects.all(),
                                                          'get_education_list': GetEducation.objects.all(),
                                                          'filter': f,
                                                          })
