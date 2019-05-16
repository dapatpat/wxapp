from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import json
# Create your views here.

def get_pageconfig(requests):
    lsConfigList = list(PageConfig.objects.all().values())
    rsData = {"data":lsConfigList}
    return JsonResponse(rsData,safe=False)