from django.http import HttpResponse, JsonResponse
from modelapp.models import Good, Say
from modelapp.models import Shop
from django.forms.models import model_to_dict
from django.db.models import F, Q, Count


# test url = http://127.0.0.1:8000/api/good?PageNo=1&PageSize=15
def good(r):
    PageNo = int(r.GET.get('PageNo'))
    PageSize = int(r.GET.get('PageSize'))
    RowCount = Good.objects.all().count()
    lsGoods = Good.objects.all()[(PageNo - 1) * PageSize:(PageNo - 1) * PageSize + PageSize]
    reLsGood = []
    for objGood in lsGoods:
        reObjGoods = {}
        reObjGoods['Say'] = list(objGood.say_set.all().values())  # 商品评论
        reObjGoods['GoodUrl'] = list(objGood.goodurl_set.all().values())  # 商品轮播图图片
        reObjGoods['GoodDetail'] = model_to_dict(objGood)  # 商品详细信息
        reObjGoods['GoodStyle'] = list(objGood.goodstyle_set.all().values())  # 商品评论
        reLsGood.append(reObjGoods)
    rs = {'Code': 200, 'Msg': '',
          'Data': {'DataSet': reLsGood, 'RowCount': RowCount, 'PageNo': PageNo, 'PageSize': PageSize}}
    return JsonResponse(rs, safe=False)


# test aip =http://127.0.0.1:8000/api/search_good?PageNo=1&PageSize=6&Search=石
def search_good(r):
    PageNo = int(r.GET.get('PageNo'))
    PageSize = int(r.GET.get('PageSize'))
    Search = r.GET.get('Search')
    RowCount = Good.objects.filter(Q(GoodName__icontains=Search) | Q(GoodCharac__icontains=Search)).count()
    lsGoods = list(Good.objects.filter(Q(GoodName__icontains=Search) | Q(GoodCharac__icontains=Search))[
                   (PageNo - 1) * PageSize:(PageNo - 1) * PageSize + PageSize].values().annotate(
        RowCount=Count('GoodID')))
    rs = {'Code': 200, 'Msg': '',
          'Data': {'DataSet': lsGoods, 'RowCount': RowCount, 'PageNo': PageNo, 'PageSize': PageSize}}
    return JsonResponse(rs, safe=False)


# test aip =http://127.0.0.1:8000/api/good_detail?GoodID=1
def good_detail(r):
    GoodID = int(r.GET.get('GoodID'))
    reObjGood = {}

    objGoodDetail = Good.objects.get(GoodID=GoodID)
    reObjGood['GoodDetail'] = model_to_dict(objGoodDetail)
    reObjGood['GoodUrl'] = list(objGoodDetail.goodurl_set.all().values())  # 商品轮播图图片
    reObjGood['Say'] = list(objGoodDetail.say_set.all().values())  # 评论
    reObjGood['GoodStyle'] = list(objGoodDetail.goodstyle_set.all().values())  # 款式
    rs = {'Code': 200, 'Msg': '', 'Data': {'DataSet': reObjGood}}
    return JsonResponse(rs, safe=False)


# http://127.0.0.1:8000/api/init_sale_type?PageNo=1&PageSize=4&GoodSaleType=1
def init_sale_type(r):
    PageNo = int(r.GET.get('PageNo'))
    PageSize = int(r.GET.get('PageSize'))
    GoodSaleType = int(r.GET.get('GoodSaleType'))  # 默认0为全查询
    if GoodSaleType != 0:
        RowCount = Good.objects.filter(GoodSaleType=GoodSaleType).count()
        reLsGood = Good.objects.filter(GoodSaleType=GoodSaleType)[
                   (PageNo - 1) * PageSize:(PageNo - 1) * PageSize + PageSize].all()
    else:  # 全查询
        RowCount = 0
        reLsGood = []
        lsGood = list(Good.objects.values('GoodSaleType').annotate(Count=Count('GoodSaleType')).order_by())
        for objGood in lsGood:
            lsGoodWithType = Good.objects.filter(GoodSaleType=objGood['GoodSaleType'])[
                             (PageNo - 1) * PageSize:(PageNo - 1) * PageSize + PageSize]
            reLsGood.append(lsGoodWithType)

    # 外联表，添加评论、轮播图等详细信息
    reLsGoods = []
    for objGood in reLsGood:
        if GoodSaleType != 0:
            reObjGoods = {}
            reObjGoods['Say'] = list(objGood.say_set.all().values())  # 商品评论
            reObjGoods['GoodUrl'] = list(objGood.goodurl_set.all().values())  # 商品轮播图图片
            reObjGoods['GoodDetail'] = model_to_dict(objGood)  # 商品详细信息
            reObjGoods['GoodStyle'] = list(objGood.goodstyle_set.all().values())  # 商品评论
            reLsGoods.append(reObjGoods)
        else:  # 全查询
            a = []
            for objGoodDetail in objGood:
                reObjGoods = {}
                reObjGoods['Say'] = list(objGoodDetail.say_set.all().values())  # 商品评论
                reObjGoods['GoodUrl'] = list(objGoodDetail.goodurl_set.all().values())  # 商品轮播图图片
                reObjGoods['GoodDetail'] = model_to_dict(objGoodDetail)  # 商品详细信息
                reObjGoods['GoodStyle'] = list(objGoodDetail.goodstyle_set.all().values())  # 商品评论
                a.append(reObjGoods)
            reLsGoods.append(a)
    rs = {'Code': 200, 'Msg': '',
          'Data': {'DataSet': reLsGoods, 'RowCount': RowCount, 'PageNo': PageNo, 'PageSize': PageSize}}
    return JsonResponse(rs, safe=False)


# 热销产品
# http://127.0.0.1:8000/api/hot_sale?PageNo=1&PageSize=4
def hot_sale(r):
    PageNo = int(r.GET.get('PageNo'))
    PageSize = int(r.GET.get('PageSize'))
    RowCount = Good.objects.filter(GoodHotSale=1).count()
    lsHotSale = list(
        Good.objects.filter(GoodHotSale=1)[(PageNo - 1) * PageSize:(PageNo - 1) * PageSize + PageSize].all().values())
    rs = {'Code': 200, 'Msg': '',
          'Data': {'DataSet': lsHotSale, 'RowCount': RowCount, 'PageNo': PageNo, 'PageSize': PageSize}}
    return JsonResponse(rs, safe=False)

