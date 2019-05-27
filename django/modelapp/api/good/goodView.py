from django.http import HttpResponse, JsonResponse
from modelapp.models import Good
from modelapp.models import Shop
from django.forms.models import model_to_dict
from django.db.models import F, Q, Count


# test url = http://127.0.0.1:8000/api/good?PageNo=1&PageSize=15
def good(r):
    PageNo = int(r.GET.get('PageNo'))
    PageSize = int(r.GET.get('PageSize'))
    RowCount = Good.objects.all().count()
    lsGoods = list(Good.objects.all()[(PageNo - 1) * PageSize:PageSize].values())
    rs = {'Code': 200, 'Msg': '',
          'Data': {'DataSet': lsGoods, 'RowCount': RowCount, 'PageNo': PageNo, 'PageSize': PageSize}}
    return JsonResponse(rs, safe=False)


# test aip =http://127.0.0.1:8000/api/search_good?PageNo=1&PageSize=6&Search=石
def search_good(r):
    PageNo = int(r.GET.get('PageNo'))
    PageSize = int(r.GET.get('PageSize'))
    Search = r.GET.get('Search')
    RowCount = Good.objects.filter(Q(GoodName__icontains=Search) | Q(GoodCharac__icontains=Search)).count()
    lsGoods = list(Good.objects.filter(Q(GoodName__icontains=Search) | Q(GoodCharac__icontains=Search))[
                   (PageNo - 1) * PageSize:PageSize].values().annotate(RowCount=Count('GoodID')))
    rs = {'Code': 200, 'Msg': '',
          'Data': {'DataSet': lsGoods, 'RowCount': RowCount, 'PageNo': PageNo, 'PageSize': PageSize}}
    return JsonResponse(rs, safe=False)


# test aip =http://127.0.0.1:8000/api/good_detail?GoodID=1
def good_detail(r):
    GoodID = int(r.GET.get('GoodID'))
    objGoodDetail = list(Good.objects.filter(GoodID__exact=GoodID).values())[0]
    rs = {'Code': 200, 'Msg': '', 'Data': {'DataSet': objGoodDetail}}
    return JsonResponse(rs, safe=False)
