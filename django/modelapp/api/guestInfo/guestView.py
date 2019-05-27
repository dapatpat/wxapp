from django.http import HttpResponse, JsonResponse
from modelapp.models import Guest,GuestReceAddress
from django.forms.models import model_to_dict


def guest_info(r):
    GuestID = r.GET.get('GuestID')
    objGuestInfo = model_to_dict(Guest.objects.filter(GuestID=GuestID))
    rs = {'Code': 200, 'Msg': '', 'DataSet': objGuestInfo}
    return JsonResponse(rs, safe=False)

# http://127.0.0.1:8000/api/add_rece_address?GuestID=1
def add_rece_address(r):
    GuestID = r.GET.get('GuestID')
    lsGuestReceAddress = list(GuestReceAddress.objects.filter(GRece_GuestID__GuestID=GuestID).all().values())
    rs = {'Code': 200, 'Msg': '', 'DataSet': lsGuestReceAddress}
    return JsonResponse(rs, safe=False)


