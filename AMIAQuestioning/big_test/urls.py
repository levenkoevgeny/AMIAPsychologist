from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'testing'

urlpatterns = [
    path('', views.test_form_add, name='test_add'),
    path('dashboard', login_required(views.dashboard), name='test_dashboard'),
    path('success', views.success, name='test_success'),
]