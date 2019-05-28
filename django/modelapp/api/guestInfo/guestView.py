from django.http import HttpResponse, JsonResponse
from modelapp.models import Guest, GuestReceAddress
from django.forms.models import model_to_dict


def guest_info(r):
    GuestID = r.GET.get('GuestID')
    objGuestInfo = model_to_dict(Guest.objects.filter(GuestID=GuestID))
    rs = {'Code': 200, 'Msg': '', 'DataSet': objGuestInfo}
    return JsonResponse(rs, safe=False)


# http://127.0.0.1:8000/api/change_guest_info
def change_guest_info(r):
    GuestID = r.POST.get('GuestID')
    GuestSex = r.POST.get('GuestSex')
    GuestName = r.POST.get('GuestName')
    GuestPhotoURL = r.POST.get('GuestPhotoURL')
    GuestRemark = r.POST.get('GuestRemark')
    try:
        if GuestID != '':
            objGuest = Guest.objects.get(GuestID=GuestID)
            objGuest.GuestSex = GuestSex
            objGuest.GuestName = GuestName
            objGuest.GuestPhotoURL = GuestPhotoURL
            objGuest.GuestRemark = GuestRemark
            objGuest.save()
        else:
            Guest.objects.create(GuestSex=GuestSex, GuestName=GuestName,
                                 GuestPhotoURL=GuestPhotoURL, GuestRemark=GuestRemark)
        rs = {'Code': 200, 'Msg': 'success'}
    except Exception:
        rs = {'Code': 500, 'Msg': 'fail'}
    return JsonResponse(rs, safe=False)


# http://127.0.0.1:8000/api/add_rece_address?GuestID=1
def get_rece_address(r):
    GuestID = r.GET.get('GuestID')
    lsGuestReceAddress = list(GuestReceAddress.objects.filter(GRece_GuestID__GuestID=GuestID).all().values())
    rs = {'Code': 200, 'Msg': '', 'DataSet': lsGuestReceAddress}
    return JsonResponse(rs, safe=False)


# http://127.0.0.1:8000/api/change_rece_address
def change_rece_address(r):
    GuestID = int(r.POST.get('GuestID'))
    Index = int(r.POST.get('Index'))
    GReceAddress = r.POST.get('GReceAddress')
    GReceTel = r.POST.get('GReceTel')
    GReceIsDefult = r.POST.get('GReceIsDefult')
    GReceRemark = r.POST.get('GReceRemark')
    GReceDistrictID = r.POST.get('GReceDistrictID')
    GReceCityID = r.POST.get('GReceCityID')
    GReceProvinceID = r.POST.get('GReceProvinceID')
    try:
        if Index != -99:  # 修改
            lsGuestReceAddress = GuestReceAddress.objects.filter(GRece_GuestID__GuestID=GuestID)[Index:Index + 1].all()
            for obj in lsGuestReceAddress:
                obj.GReceAddress = GReceAddress
                obj.GReceTel = GReceTel
                obj.GReceIsDefult = GReceIsDefult
                obj.GReceRemark = GReceRemark
                obj.GReceCityID = GReceCityID
                obj.GReceProvinceID = GReceProvinceID
                obj.GReceDistrictID = GReceDistrictID
                obj.save()
            rs = {'Code': 200, 'Msg': 'up success'}
        else:  # 新增
            GuestReceAddress.objects.create(GReceAddress=GReceAddress, GReceTel=GReceTel, GReceIsDefult=GReceIsDefult,
                                            GReceRemark=GReceRemark, GRece_GuestID_id=1, GReceCityID=GReceCityID,
                                            GReceProvinceID=GReceProvinceID, GReceDistrictID=GReceDistrictID)
            rs = {'Code': 200, 'Msg': 'add success'}
    except:
        rs = {'Code': 500, 'Msg': 'fail'}
    return JsonResponse(rs, safe=False)


# http://127.0.0.1:8000/api/del_rece_address?GuestID=1&Index=0
def del_rece_address(r):
    GuestID = int(r.GET.get('GuestID'))
    Index = int(r.GET.get('Index'))
    try:
        lsGuestReceAddress = GuestReceAddress.objects.filter(GRece_GuestID__GuestID=GuestID)[Index:Index + 1].all()
        for obj in lsGuestReceAddress:
            obj.delete()
        rs = {'Code': 200, 'Msg': 'del success'}
    except:
        rs = {'Code': 500, 'Msg': 'fail'}
    return JsonResponse(rs, safe=False)


# http://127.0.0.1:8000/api/defult_rece_address?GuestID=1&Index=0&GReceIsDefult=0
def defult_rece_address(r):
    GuestID = int(r.GET.get('GuestID'))
    Index = int(r.GET.get('Index'))
    GReceIsDefult = int(r.GET.get('GReceIsDefult'))
    try:
        lsGuestReceAddress = GuestReceAddress.objects.filter(GRece_GuestID__GuestID=GuestID)[Index:Index + 1].all()
        lsAllGuestReceAddress = GuestReceAddress.objects.filter(GRece_GuestID__GuestID=GuestID).all()
        for obj in lsAllGuestReceAddress:  # 先全部设置为0
            obj.GReceIsDefult = 0
            obj.save()
        for obj in lsGuestReceAddress:  # 再设置对应index为1
            obj.GReceIsDefult = GReceIsDefult
            obj.save()
        rs = {'Code': 200, 'Msg': 'del success'}
    except:
        rs = {'Code': 500, 'Msg': 'fail'}
    return JsonResponse(rs, safe=False)
