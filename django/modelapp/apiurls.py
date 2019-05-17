from django.contrib import admin
from django.urls import path
from modelapp import views

urlpatterns = [
    path('get_pageconfig', views.get_pageconfig),
    path('get_swiper', views.get_swiper),
    path('init_page',views.init_page),
]

