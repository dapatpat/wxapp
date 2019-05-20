# Generated by Django 2.2.1 on 2019-05-20 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('ArticleID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('ArticleName', models.CharField(max_length=120, null=True)),
                ('ArticleTime', models.DateField(null=True)),
                ('ArticleLikeCount', models.IntegerField(default=0, null=True)),
                ('ArticleReadCount', models.IntegerField(default=0, null=True)),
                ('ArticleAuthor', models.CharField(max_length=120, null=True)),
                ('ArticleDetail', models.TextField(max_length=1000, null=True)),
                ('ArticleIntroduc', models.CharField(max_length=220, null=True)),
                ('ArticleRemark', models.CharField(max_length=220, null=True)),
                ('ArticleType', models.IntegerField(null=True)),
                ('ArticleTypeName', models.DateField(max_length=120, null=True)),
                ('ArticleCreateTime', models.DateField(null=True)),
            ],
            options={
                'db_table': 'Article',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('CityID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('CityName', models.CharField(max_length=120, null=True)),
                ('IsCapitalCity', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('DictID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('DitcType', models.IntegerField(null=True)),
                ('DitcTypeName', models.CharField(max_length=120, null=True)),
                ('DictNo', models.IntegerField(null=True)),
                ('DictName', models.CharField(max_length=120, null=True)),
                ('DictValue', models.DateField(max_length=120, null=True)),
                ('DictSort', models.IntegerField(null=True)),
                ('DictFlay', models.IntegerField(default=1, null=True)),
                ('DictCreateTime', models.DateField(null=True)),
            ],
            options={
                'db_table': 'Dict',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('GoodID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('GoodType', models.IntegerField(null=True)),
                ('GoodTypeName', models.CharField(max_length=120, null=True)),
                ('GoodSaleType', models.IntegerField(null=True)),
                ('GoodSaleTypeName', models.CharField(max_length=120, null=True)),
                ('GoodName', models.CharField(max_length=120, null=True)),
                ('GoodSubtitle', models.CharField(max_length=120, null=True)),
                ('GoodCharac', models.CharField(max_length=120, null=True)),
                ('GoodIntroduct', models.CharField(max_length=220, null=True)),
                ('GoodOrigiPrice', models.CharField(max_length=120, null=True)),
                ('GoodSaleCount', models.IntegerField(default=0, null=True)),
                ('GoodSalePrice', models.CharField(max_length=120, null=True)),
                ('GoodDiscount', models.CharField(max_length=120, null=True)),
                ('GoodDetail', models.TextField(max_length=1120, null=True)),
                ('GoodInstockCount', models.IntegerField(default=0, null=True)),
                ('GoodLikeCount', models.IntegerField(default=0, null=True)),
                ('GoodSaveCount', models.IntegerField(default=0, null=True)),
                ('GoodVipPoint', models.IntegerField(default=0, null=True)),
                ('GoodRemark', models.CharField(max_length=220, null=True)),
                ('GoodCreateTime', models.DateField(max_length=120, null=True)),
            ],
            options={
                'db_table': 'Good',
            },
        ),
        migrations.CreateModel(
            name='GoodGoodStyleRela',
            fields=[
                ('GGSGoodGStyleID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('GGSRemark', models.CharField(max_length=112, null=True)),
                ('GGSCreateTime', models.DateField(null=True)),
            ],
            options={
                'db_table': 'GoodGoodStyleRela',
            },
        ),
        migrations.CreateModel(
            name='GoodStyle',
            fields=[
                ('GStyleID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('GStyleType', models.IntegerField(null=True)),
                ('GStyleTypeName', models.CharField(max_length=112, null=True)),
                ('GStyleDetail', models.CharField(max_length=112, null=True)),
                ('GStyleRemark', models.CharField(max_length=212, null=True)),
                ('GStyleCreateTime', models.DateField(null=True)),
                ('GStyle_GoodID', models.ManyToManyField(through='modelapp.GoodGoodStyleRela', to='modelapp.Good')),
            ],
            options={
                'db_table': 'GoodStyle',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('GuestID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('GuestType', models.IntegerField(null=True)),
                ('GuestTypeName', models.CharField(max_length=40, null=True)),
                ('GuestDocType', models.IntegerField(null=True)),
                ('GuestDocTypeName', models.CharField(max_length=20, null=True)),
                ('GuestDocNo', models.CharField(max_length=40, null=True)),
                ('GuestDocName', models.CharField(max_length=40, null=True)),
                ('GuestName', models.CharField(max_length=140, null=True)),
                ('GuestBornDate', models.DateField(max_length=40, null=True)),
                ('GuestSex', models.IntegerField(default=0, null=True)),
                ('GuestNativePlace', models.CharField(max_length=40, null=True)),
                ('GuestNation', models.CharField(max_length=40, null=True)),
                ('GuestStatus', models.CharField(max_length=40, null=True)),
                ('GuestResAddress', models.CharField(max_length=140, null=True)),
                ('GuestPhotoURL', models.CharField(max_length=240, null=True)),
                ('GuestRemark', models.CharField(max_length=140, null=True)),
                ('GuestMoney', models.CharField(max_length=120, null=True)),
                ('GuestCreateTime', models.DateField(null=True)),
            ],
            options={
                'db_table': 'Guest',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('OrderCode', models.CharField(max_length=120, null=True)),
                ('OrderType', models.IntegerField(null=True)),
                ('OrderTypeName', models.CharField(max_length=120, null=True)),
                ('OrderAmount', models.CharField(max_length=120, null=True)),
                ('OrderPayAmount', models.CharField(max_length=120, null=True)),
                ('OrderPayTime', models.DateField(max_length=120, null=True)),
                ('OrderTradeNo', models.CharField(max_length=120, null=True)),
                ('OrderCreateTime', models.DateField(max_length=120, null=True)),
                ('OrderRemark', models.CharField(max_length=120, null=True)),
                ('OrderDeliType', models.IntegerField(default=0, null=True)),
                ('OrderDeliCost', models.CharField(max_length=120, null=True)),
                ('OrderInCar', models.IntegerField(default=1, null=True)),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='PageConfig',
            fields=[
                ('ConfigID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('ConfigDataType', models.IntegerField(null=True, verbose_name='数据分类')),
                ('ConfigType', models.IntegerField(null=True)),
                ('ConfigTypeNmae', models.CharField(max_length=120, null=True)),
                ('ConfigKeyNo', models.IntegerField(null=True)),
                ('ConfigKeyName', models.CharField(max_length=120, null=True)),
                ('ConfigKeyValue', models.CharField(max_length=120, null=True)),
                ('ConfigFlag', models.BooleanField(default=True, null=True)),
                ('ConfigCreatTime', models.DateField(default=False, null=True)),
            ],
            options={
                'verbose_name_plural': '配置表',
                'db_table': 'myapp_pageconfig',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('ProvinceID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('ProvinceName', models.CharField(max_length=120, null=True)),
            ],
            options={
                'db_table': 'Province',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('ShopID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('ShopName', models.CharField(max_length=120, null=True)),
                ('ShopHeadUrl', models.CharField(max_length=120, null=True)),
                ('ShopResponName', models.CharField(max_length=120, null=True)),
                ('ShopResponDocNo', models.CharField(max_length=120, null=True)),
                ('ShopResponDocType', models.IntegerField(null=True)),
                ('ShopResponDocTypeName', models.CharField(max_length=120, null=True)),
                ('ShopResponTel', models.CharField(max_length=120, null=True)),
                ('ShopTel', models.CharField(max_length=120, null=True)),
                ('ShopPhone', models.CharField(max_length=120, null=True)),
                ('ShopIntroduct', models.CharField(max_length=120, null=True)),
                ('ShopDetail', models.CharField(max_length=220, null=True)),
                ('ShopAddress', models.CharField(max_length=120, null=True)),
                ('ShopLongitude', models.CharField(max_length=120, null=True)),
                ('ShopLatitude', models.CharField(max_length=120, null=True)),
                ('ShopBusinessPermitNo', models.CharField(max_length=120, null=True)),
                ('ShopBusinessPermitUrl', models.CharField(max_length=120, null=True)),
                ('ShopHealthPermitNo', models.CharField(max_length=120, null=True)),
                ('ShopHealthPermiUrl', models.CharField(max_length=120, null=True)),
                ('ShopRemark', models.CharField(max_length=120, null=True)),
                ('ShopCreateTime', models.CharField(max_length=120, null=True)),
            ],
            options={
                'db_table': 'Shop',
            },
        ),
        migrations.CreateModel(
            name='Swiper',
            fields=[
                ('SwiperID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('SwiperUrl', models.CharField(max_length=120, null=True)),
                ('SwiperType', models.IntegerField(null=True)),
                ('SwiperTypeName', models.CharField(max_length=120, null=True)),
                ('SwiperIsFlat', models.IntegerField(default=1, null=True)),
                ('SwiperCreateTime', models.DateField(null=True)),
            ],
            options={
                'db_table': 'Swiper',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('UserName', models.CharField(max_length=222, null=True)),
                ('UsePassword', models.CharField(max_length=220, null=True)),
                ('UseTel', models.CharField(max_length=220, null=True)),
                ('UseState', models.IntegerField(null=True)),
                ('UseStateName', models.CharField(max_length=220, null=True)),
                ('UserDocNo', models.CharField(max_length=220, null=True)),
                ('UserDocType', models.IntegerField(default=1, null=True)),
                ('UserDocTypeName', models.CharField(max_length=220, null=True)),
                ('UserPost', models.CharField(max_length=220, null=True)),
                ('UserCreateTime', models.DateField(null=True)),
                ('UserRemark', models.CharField(max_length=123, null=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Vip',
            fields=[
                ('VipID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('VipType', models.IntegerField(default=0, null=True)),
                ('VipiTypeName', models.CharField(max_length=120, null=True)),
                ('VipPoint', models.IntegerField(default=0, null=True)),
                ('VipRemark', models.CharField(max_length=120, null=True)),
                ('ViprCreateTime', models.DateField(null=True)),
                ('Guest_VipID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Guest')),
            ],
            options={
                'db_table': 'Vip',
            },
        ),
        migrations.CreateModel(
            name='Say',
            fields=[
                ('SayID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('SayType', models.IntegerField(default=0, null=True)),
                ('SayTypeName', models.CharField(max_length=12, null=True)),
                ('SayDetail', models.TextField(max_length=1002, null=True)),
                ('SayRemark', models.CharField(max_length=112, null=True)),
                ('SayCreateTime', models.DateField(null=True)),
                ('Say_GoodID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Good')),
            ],
            options={
                'db_table': 'Say',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('OStatusID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('OStatusType', models.IntegerField(null=True)),
                ('OStatusTypeName', models.CharField(max_length=120, null=True)),
                ('OStatusValue', models.CharField(max_length=120, null=True)),
                ('OStatusRemark', models.CharField(max_length=120, null=True)),
                ('OStatusCreatTime', models.DateField(max_length=120, null=True)),
                ('OstatusDeliTime', models.DateField(max_length=120, null=True)),
                ('OstatusReceTime', models.DateField(max_length=120, null=True)),
                ('OStatus_OrderID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Order')),
            ],
            options={
                'db_table': 'OrderStatus',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('ODetailID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('ODetailCode', models.CharField(max_length=120, null=True)),
                ('ODetailGoodCount', models.IntegerField(null=True)),
                ('ODetailOriginPrice', models.CharField(max_length=120, null=True)),
                ('ODetailSalePrice', models.CharField(max_length=120, null=True)),
                ('ODetailSaleAmount', models.CharField(max_length=120, null=True)),
                ('ODetailRemark', models.CharField(max_length=120, null=True)),
                ('OrderCreateTime', models.DateField(max_length=120, null=True)),
                ('ODetail_GStyleID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.GoodStyle')),
                ('ODetail_GoodID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Good')),
                ('ODetail_GuestID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Guest')),
                ('ODetailr_OrderID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Order')),
            ],
            options={
                'db_table': 'OrderDetail',
            },
        ),
        migrations.CreateModel(
            name='GuestReceAddress',
            fields=[
                ('GReceID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('GReceAddress', models.CharField(max_length=222, null=True)),
                ('GReceTel', models.CharField(max_length=220, null=True)),
                ('GReceIsDefult', models.IntegerField(default=0, null=True)),
                ('GReceIsFlat', models.IntegerField(default=1, null=True)),
                ('GReceRemark', models.CharField(max_length=220, null=True)),
                ('GReceCreateTime', models.DateField(null=True)),
                ('GRece_GuestID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Guest')),
            ],
            options={
                'db_table': 'GuestReceAddress',
            },
        ),
        migrations.CreateModel(
            name='GoodUrl',
            fields=[
                ('GUrlID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('GUrlUrl', models.CharField(max_length=220, null=True)),
                ('GUrlMain', models.IntegerField(default=0, null=True)),
                ('GUrlRemark', models.CharField(max_length=112, null=True)),
                ('GUrlCreateTime', models.DateField(max_length=12, null=True)),
                ('GUrl_GoodID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Good')),
            ],
            options={
                'db_table': 'GoodUrl',
            },
        ),
        migrations.AddField(
            model_name='goodgoodstylerela',
            name='GGSGStyleID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='modelapp.GoodStyle'),
        ),
        migrations.AddField(
            model_name='goodgoodstylerela',
            name='GGSGoodID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='modelapp.Good'),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('DistrictID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('DistrictName', models.CharField(max_length=120, null=True)),
                ('CityID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.City')),
                ('ProvinceID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Province')),
            ],
            options={
                'db_table': 'District',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='ProvinceID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelapp.Province'),
        ),
    ]
