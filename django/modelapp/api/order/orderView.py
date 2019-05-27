from django.http import HttpResponse, JsonResponse
from modelapp.models import Guest
from modelapp.models import OrderDetail
from modelapp.models import Order, OrderStatus
from django.forms.models import model_to_dict
from django.db.models import F, Q


# http://127.0.0.1:8000/api/order?GuestID=1&OStatusType=0&PageNo=1&PageSize=10
def order(r):
    GuestID = int(r.GET.get('GuestID'))
    OStatusType = int(r.GET.get('OStatusType'))  # 0 为全查询
    PageNo = int(r.GET.get('PageNo'))
    PageSize = int(r.GET.get('PageSize'))
    if OStatusType != 0:                                                    # 反向查询
        lsOrder = Order.objects.filter(Q(Order_GuestID=GuestID) & Q(orderstatus__OStatusType=OStatusType))  # 获取该用户下所有订单
    else:
        lsOrder = Order.objects.filter(Order_GuestID=GuestID)  # 获取该用户下所有订单
    RowCount = Order.objects.filter(Order_GuestID=GuestID).count()  # 用户的总订单数
    rsLsOrder = []
    for objOrder in lsOrder:
        # 获取每张订单下的订单详情
        rsObjOrder = {}
        lsOrderDetail = objOrder.orderdetail_set.all()  # 反向查询
        reLsOrderDetail = []
        for objOrderDetail in lsOrderDetail:
            rsObjOrderDetail = {}
            rsObjOrderDetail['Order'] = model_to_dict(objOrder)  # 订单表 订单信息 #正向查询
            rsObjOrderDetail['OrderDetail'] = model_to_dict(objOrderDetail)  # 订单表 订单详细信息
            rsObjOrderDetail['Good'] = model_to_dict(objOrderDetail.ODetail_GoodID)  # 订单下的商品信息
            rsObjOrderDetail['objGoodStyle'] = model_to_dict(objOrderDetail.ODetail_GStyleID)  # 订单下的商品款式
            reLsOrderDetail.append(rsObjOrderDetail)
        rsObjOrder['OrderDetail'] = reLsOrderDetail

        # 获取每张订单下经历过的订单状态状态
        if OStatusType == 0:                                # 全部订单状态查询  正向查询
            lsOrderStatus = OrderStatus.objects.filter(OStatus_OrderID__OrderID=objOrder.OrderID)
        else:
            lsOrderStatus = OrderStatus.objects.filter(
                Q(OStatusType=OStatusType) & Q(OStatus_OrderID__OrderID=objOrder.OrderID))
        reLsOrderStatus = []
        for objOrderStatus in lsOrderStatus:
            reLsOrderStatus.append(model_to_dict(objOrderStatus))
        rsObjOrder['OrderStatus'] = reLsOrderStatus
        rsLsOrder.append(rsObjOrder)

    rs = {'Code': 200, 'Msg': '',
          'Data': {'DataSet': rsLsOrder, 'PageNo': PageNo, 'PageSize': PageSize, 'RowCount': RowCount}}
    return JsonResponse(rs, safe=False)
