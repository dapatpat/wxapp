from django.contrib import admin
from django.urls import path
from modelapp import views
from modelapp.api.config import confView
from modelapp.api.shop import shopView
from modelapp.api.good import goodView
from modelapp.api.article import articleView
from modelapp.api.guestInfo import guestView
from modelapp.api.order import orderView

urlpatterns = [
    path('get_pageconfig', confView.get_pageconfig),  # 页面初始化数据
    path('get_swiper', shopView.get_swiper),
    path('shop', shopView.shop),
    path('init_page', views.init_page),
    path('get_dict', confView.get_dict),  # 字典数据
    path('good', goodView.good),  #获取商品列表
    path('search_good', goodView.search_good),  #获取商品列表
    path('good_detail', goodView.good_detail),  #获取商品详情
    path('init_article', articleView.init_article),  #获取文章列表
    path('guest_info', guestView.guest_info),  #获取客人信息
    path('order', orderView.order),  #获取文章列表
]
