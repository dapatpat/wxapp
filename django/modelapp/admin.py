from django.contrib import admin
from modelapp.models import *


# Register your models here.

class MyConfig(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ("ConfigID", "ConfigDataType", "ConfigType", "ConfigTypeNmae", "ConfigKeyNo",
                    "ConfigKeyName", "ConfigKeyValue", "ConfigFlag", "ConfigCreatTime")


admin.site.register(Article)
# admin.site.register(auth_group)
# admin.site.register(auth_group_permissions)
# admin.site.register(auth_permission)
# admin.site.register(auth_user)
# admin.site.register(auth_user_groups)
# admin.site.register(auth_user_user_permissions)
# admin.site.register(city)
# admin.site.register(dict)
# admin.site.register(district)
# admin.site.register(django_admin_log)
# admin.site.register(django_content_type)
# admin.site.register(django_migrations)
# admin.site.register(django_session)
# admin.site.register(good)
# admin.site.register(goodgoodstylerela)
# admin.site.register(goodstyle)
# admin.site.register(goodurl)
# admin.site.register(guest)
# admin.site.register(guestreceaddress)
admin.site.register(PageConfig, MyConfig)
# admin.site.register(order)
# admin.site.register(orderdetail)
# admin.site.register(orderstatus)
# admin.site.register(province)
# admin.site.register(say)
# admin.site.register(shop)
admin.site.register(Swiper)
# admin.site.register(user)
# admin.site.register(vip)
