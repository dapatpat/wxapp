from django.contrib import admin
from django.urls import path
from modelapp import views
from modelapp.api.config import confView
from modelapp.api.shop import shopView

urlpatterns = [
    path('get_pageconfig', confView.get_pageconfig),
    path('get_swiper', shopView.get_swiper),
    path('init_page', views.init_page),
]
