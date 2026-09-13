from django.urls import path

from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('semana/', views.semana, name='semana'),
]