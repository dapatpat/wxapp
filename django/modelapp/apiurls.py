from django.contrib import admin
from django.urls import path
from modelapp import views
from modelapp.api.config import confView
from modelapp.api.shop import shopView
from modelapp.api.good import goodView

urlpatterns = [
    path('get_pageconfig', confView.get_pageconfig),  # 页面初始化数据
    path('get_swiper', shopView.get_swiper),
    path('shop', shopView.shop),
    path('init_page', views.init_page),
    path('get_dict', confView.get_dict),  # 字典数据
    path('good', goodView.good),  #获取商品列表
    path('search_good', goodView.search_good),  #获取商品列表
    path('good_detail', goodView.good_detail),  #获取商品列表
]
