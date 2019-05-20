from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json


# Create your views here.

# def get_pageconfig(requests):
#     '''获取配置参数'''
#     lsConfigList = list(PageConfig.objects.all().values())
#     rsData = {"data": lsConfigList}
#     return JsonResponse(rsData, safe=False)


def get_swiper(requests):
    '''获取轮播图信息'''
    lsSwiper = list(Swiper.objects.all().values())
    rsData = {"data": lsSwiper}
    return JsonResponse(rsData, safe=False)


def init_page(request):
    """返回全部"""
    lsParList = request.GET.get("paramerslist", []).replace('[', '').replace("]", '').split(",")
    print(lsParList)
    resList = []
    rsData = {'data': {}}
    if (lsParList):
        try:
            for par in lsParList:
                rsData["data"]['ls' + par] = eval('list(%s.objects.all().values())' % (par))
        except Exception as e:
            rsData['errmsg'] = str(e)
            rsData['errcode'] = "401"
    return JsonResponse(rsData, safe=False)
