from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('returnbox', views.returnbox, name='returnbox')

]
