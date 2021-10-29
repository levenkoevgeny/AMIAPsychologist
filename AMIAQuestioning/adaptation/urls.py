from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'adaptation'

urlpatterns = [
    path('', views.adaptation_add, name='adaptation_add'),
    path('success', views.success, name='adaptation_success'),
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
]