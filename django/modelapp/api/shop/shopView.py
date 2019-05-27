from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from modelapp.models import Swiper
from modelapp.models import Shop
from django.forms.models import model_to_dict
import json


def get_swiper(requests):
    '''获取轮播图信息'''
    lsSwiper = list(Swiper.objects.all().values())
    rsData = {"data": lsSwiper}
    return JsonResponse(rsData, safe=False)


def shop(r):
    objShop = model_to_dict(Shop.objects.first())
    rs = {'Code': 200, 'Msg': '', 'DataSet': objShop}
    return JsonResponse(rs, safe=False)
