from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('returnbox', views.returnbox, name='returnbox'),
    path('box_return_request', views.box_return_request, name='box_return_request'),
    path('remove_box_return/<int:box_return_id>/', views.remove_box_return, name='remove_box_return'),
]
