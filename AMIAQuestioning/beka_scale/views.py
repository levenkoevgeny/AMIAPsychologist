from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Question, BekaScale, Result, Position
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def test_form_add(request):
    if request.method == 'POST':
        beka_new = BekaScale(
            fio=request.POST['fio'],
            group=request.POST['group'],
            position=get_object_or_404(Position, pk=request.POST['position'])
        )
        beka_new.save()
        for question_loop in Question.objects.all():
            result = Result(
                beka_scale=beka_new,
                question=question_loop,
                answer=request.POST['question_' + str(question_loop.id) + '_radio']
            )
            result.save()
        return HttpResponseRedirect(reverse('beka_scale:test_success'))
    else:
        question_list = Question.objects.all()
        position_list = Position.objects.all()
        return render(request, 'beka_scale/beka_scale_input_form.html',
                      {'question_list': question_list,
                       'position_list': position_list
                       })


def dashboard(request):
    result_list = Result.objects.all().order_by('beka_scale__fio')
    question_list = Question.objects.all()
    questionary_list = BekaScale.objects.all()

    return render(request, 'beka_scale/dashboard.html', {
        'result_list': result_list,
        'question_list': question_list,
        'questionary_list': questionary_list,
    })


def success(request):
    return render(request, 'beka_scale/success.html')
