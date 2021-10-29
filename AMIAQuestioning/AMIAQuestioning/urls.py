from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('questioning/', include('questioning.urls')),
    path('course/', include('course.urls')),
    path('graduate/', include('graduate.urls')),
    path('big_test/', include('big_test.urls')),
    path('adaptation/', include('adaptation.urls')),
    path('beka/', include('beka_scale.urls')),
    path('personal-work/', include('personalwork.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    # path('', RedirectView.as_view(url='/questioning'), name='index'),
    # path('results/', TemplateView.as_view(template_name="index.html"), name='results'),
    path('accounts/', include('django.contrib.auth.urls'))
]
