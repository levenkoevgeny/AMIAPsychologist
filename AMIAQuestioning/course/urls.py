from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'course'

urlpatterns = [
    path('', views.questioning_add, name='add'),
    path('success/', views.success, name='success'),
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
]