from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro),
    path('login/', views.loginfront),
    path('', views.index),

]