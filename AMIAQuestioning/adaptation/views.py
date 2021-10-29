from django.shortcuts import render
from django.utils import timezone

from .forms import AdaptationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Adaptation, Tension
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def adaptation_add(request):
    if request.method == 'POST':
        form = AdaptationForm(request.POST)
        if form.is_valid():
            adaptation = form.save()
            adaptation.date_added = timezone.now()
            adaptation.save()
            return HttpResponseRedirect(reverse('adaptation:adaptation_success'))
        else:
            return render(request, 'adaptation/adaptation_input_form.html', {'form': form})
    else:
        form = AdaptationForm
        return render(request, 'adaptation/adaptation_input_form.html', {'form': form})


def success(request):
    return render(request, 'adaptation/success.html')


def dashboard(request):
    dashboard_list = Adaptation.objects.all()
    tensions_list = Tension.objects.all()
    return render(request, 'adaptation/dashboard.html', {
        'dashboard_list': dashboard_list,
        'tensions_list': tensions_list
    })