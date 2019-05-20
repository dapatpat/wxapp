from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from modelapp.models import Swiper
import json


def get_swiper(requests):
    '''获取轮播图信息'''
    lsSwiper = list(Swiper.objects.all().values())
    rsData = {"data": lsSwiper}
    return JsonResponse(rsData, safe=False)