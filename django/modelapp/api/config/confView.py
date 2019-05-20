from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sys
sys.path.append('../../modelapp/')
from modelapp.models import PageConfig
import json

def get_pageconfig(requests):
    '''获取配置参数'''
    print('1')
    lsConfigList = list(PageConfig.objects.all().values())
    rsData = {"data": lsConfigList}

    return JsonResponse(rsData, safe=False)
