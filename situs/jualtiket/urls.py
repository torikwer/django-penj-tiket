from django.urls import path

from . import views

app_name = 'jualtiket'

urlpatterns = [
    path('', views.index, name='index'),
    ]
    
