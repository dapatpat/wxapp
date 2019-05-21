from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseServerError
from modelapp.log.param_log import log
import sys
from modelapp.models import PageConfig
from modelapp.models import Dict
import json


def get_pageconfig(requests):
    '''获取配置参数'''
    lsConfigList = list(PageConfig.objects.all().values())
    rsData = {"data": lsConfigList}

    return JsonResponse(rsData, safe=False)

@log
def get_dict(requests):
    lsConfigDatas = list(Dict.objects.all().values())
    data = {'data': lsConfigDatas, 'code': 200}
    return JsonResponse(data)
