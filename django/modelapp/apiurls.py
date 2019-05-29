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
    path('good', goodView.good),  #商品列表
    path('search_good', goodView.search_good),  #，模糊查询商品列表
    path('good_detail', goodView.good_detail),  #商品详情
    path('init_article', articleView.init_article),  #文章列表
    path('guest_info', guestView.guest_info),  #客人信息
    path('order', orderView.order),  #订单列表
    path('init_sale_type', goodView.init_sale_type),  #不同销售类型商品初始化和查询
    path('get_rece_address', guestView.get_rece_address),  #不同销售类型商品初始化和查询
    path('change_guest_info', guestView.change_guest_info),  #新增或更改个人信息
    path('change_rece_address', guestView.change_rece_address),  #新增或修改快递地址
    path('defult_rece_address', guestView.defult_rece_address),  #修改默认快递收货地址
    path('make_order', orderView.make_order),  #生成订单
]
