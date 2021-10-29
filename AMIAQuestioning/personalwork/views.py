from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import PersonalWorkFilter
from .models import PersonalWork, Subdivision
from .forms import PersonalWorkForm


@login_required
def work_list(request):
    path = str(request.get_full_path())
    request.session['next_path'] = path
    if request.user.is_superuser:
        works_list = PersonalWork.objects.all()
    else:
        works_list = PersonalWork.objects.filter(executor=request.user)
    f = PersonalWorkFilter(request.GET, queryset=works_list)
    return render(request, 'personalwork/work_list.html',
                  {'works_list': f.qs,
                   'filter': f
                   })


@login_required
def work_input(request):
    if request.method == 'POST':
        form = PersonalWorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.executor = request.user
            work.save()
            if 'next_path' in request.session:
                return HttpResponseRedirect(request.session.get('next_path'))
            else:
                return HttpResponseRedirect(reverse('personalwork:work_list'))
    else:
        form = PersonalWorkForm(initial={'work_date': datetime.now()})
        return render(request, 'personalwork/work_input_form.html', {'form': form})


@login_required
def work_update(request, work_id):
    if request.method == 'POST':
        obj = get_object_or_404(PersonalWork, pk=work_id)
        form = PersonalWorkForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            if 'next_path' in request.session:
                return HttpResponseRedirect(request.session.get('next_path'))
            else:
                return HttpResponseRedirect(reverse('personalwork:work_list'))
        else:
            return render(request, 'personalwork/work_update_form.html', {'form': form, 'work': obj})
    else:
        work = get_object_or_404(PersonalWork, pk=work_id)
        form = PersonalWorkForm(instance=work)
    return render(request, 'personalwork/work_update_form.html', {'form': form, 'work': work})


# def get_subdivisions(request):
#     import requests
#     r = requests.get('http://192.168.0.124/api/subdivisions/')
#     items = r.json()
#
#     for item in items:
#         subdivision = Subdivision(subdivision_title=item['subdivision_name'])
#         subdivision.save()
#
#     return JsonResponse({'old': 'success'}, safe=False)






