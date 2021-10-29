from django.shortcuts import render
from .forms import AnketaForm
from .models import *
from django.http import HttpResponseRedirect

from django.urls import reverse
from .filters import CourseFilter
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def questioning_add(request):
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            anketa = form.save(commit=False)
            anketa.education = request.POST.get('education')
            anketa.military = request.POST.get('military')
            anketa.marriage = request.POST.get('marriage')
            anketa.parents = request.POST.get('parents')
            anketa.parents_in_marriage_live = request.POST.get('parents_in_marriage_live')
            anketa.parents_not_in_marriage_live = request.POST.get('parents_not_in_marriage_live')
            if 'mother_father1' in request.POST:
                anketa.mother_father = get_object_or_404(MotherFather, pk=request.POST.get('mother_father1'))
            if 'mother_father2' in request.POST:
                anketa.mother_father = get_object_or_404(MotherFather, pk=request.POST.get('mother_father2'))
            if 'stepmother_stepfather1' in request.POST:
                anketa.stepmother_stepfather = get_object_or_404(StepmotherStepfather, pk=request.POST.get('stepmother_stepfather1'))
            if 'stepmother_stepfather2' in request.POST:
                anketa.stepmother_stepfather = get_object_or_404(StepmotherStepfather, pk=request.POST.get('stepmother_stepfather2'))
            anketa.sport_level = request.POST.get('sport_level')
            anketa.gaming = request.POST.get('gaming')
            anketa.smoking = request.POST.get('smoking')

            anketa.save()

            form.save_m2m()

            return HttpResponseRedirect(reverse('course:success'))
        else:
            return render(request, 'course/input_form.html', {'form': form})
    else:
        form = AnketaForm
        return render(request, 'course/input_form.html', {'form': form,
                                                          })


def dashboard(request):
    f = CourseFilter(request.GET, queryset=Anketa.objects.all())
    paginator = Paginator(f.qs, 1000)
    page = request.GET.get('page')
    subjects = paginator.get_page(page)
    return render(request, 'course/dashboard.html', {'list': subjects,
                                                     'filter': f,
                                                     })


def success(request):
    return render(request, 'course/success.html')