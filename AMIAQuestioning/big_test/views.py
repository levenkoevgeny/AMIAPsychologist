from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Questionary, Result, TestKind
from django.urls import reverse
from django.views.decorators.cache import cache_page
from course.models import Group


def test_form_add(request):
    if request.method == 'POST':
        questionary_new = Questionary(
            fio=request.POST['fio'],
            group=get_object_or_404(Group, pk=request.POST['group']),
            kind=get_object_or_404(TestKind, pk=1),
            date_of_birth=request.POST.get('date_of_birth'),
            timer=request.POST.get('timer', 0)
        )
        questionary_new.save()
        for question_loop in Question.objects.all():
            result = Result(
                questionary=questionary_new,
                question=question_loop,
                answer=request.POST['question_' + str(question_loop.id) + '_radio']
            )
            result.save()
        return HttpResponseRedirect(reverse('testing:test_success'))
    else:
        question_list = Question.objects.all()
        group_list = Group.objects.all()
        return render(request, 'testing/test_input_form.html',
                      {'question_list': question_list,
                       'group_list': group_list,
                       })


def dashboard(request):
    result_list = Result.objects.all().order_by('questionary__fio')
    question_list = Question.objects.all()
    questionary_list = Questionary.objects.all()

    return render(request, 'testing/dashboard.html', {
        'result_list': result_list,
        'question_list': question_list,
        'questionary_list': questionary_list,
    })


def success(request):
    return render(request, 'testing/success.html')
