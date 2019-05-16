from django.contrib import admin
from django.urls import path
from modelapp import views

urlpatterns = [
    path('get_pageconfig', views.get_pageconfig),
]
