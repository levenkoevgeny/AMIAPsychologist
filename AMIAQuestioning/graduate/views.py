from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GraduatingForm
from .models import GraduateForm
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def graduate_add(request):
    if request.method == 'POST':
        form = GraduatingForm(request.POST)
        if form.is_valid():
            anketa = form.save()
            return HttpResponseRedirect(reverse('graduate:success'))
        else:
            return render(request, 'graduate/input_form.html', {'form': form})
    else:
        form = GraduatingForm
        return render(request, 'graduate/input_form.html', {'form': form,
                                                            })


def success(request):
    return render(request, 'graduate/success.html')


def dashboard(request):
    results = GraduateForm.objects.all()
    return render(request, 'graduate/dashboard.html', {'results': results})