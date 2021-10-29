from django.urls import path
from . import views


app_name = 'personalwork'

urlpatterns = [
    path('', views.work_list, name='work_list'),
    path('add', views.work_input, name='work_input'),
    path('<work_id>/update', views.work_update, name='work_update'),
    # path('subdivisions', views.get_subdivisions, name='work_update'),
]