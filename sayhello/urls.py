from . import views

from django.urls import path

urlpatterns = [
    path('getdata/hi/', views.hi, name='hi'),
    path('', views.homme, name='home'),
    path('getdata/', views.getdata, name='getdata'),



]