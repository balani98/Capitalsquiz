from django.urls import path

from . import views

urlpatterns = [
    path('', views.capitalsquiz, name='capitalsquiz'),
    path('ajax/validate/', views.validateCapital, name='validateCapital'),
]