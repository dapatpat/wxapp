from django.http import HttpResponse, JsonResponse
from modelapp.models import Guest
from django.forms.models import model_to_dict


def guest_info(r):
    objGuestInfo = model_to_dict(Guest.objects.first())
    rs = {'Code': 200, 'Msg': '', 'DataSet': objGuestInfo}
    return JsonResponse(rs, safe=False)



