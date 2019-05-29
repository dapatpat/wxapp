from django.db import models


class PageConfig(models.Model):
    ConfigID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    ConfigDataType = models.IntegerField(null=True, verbose_name='数据分类')  # 数据分类  (如 分类：1 数组 )
    ConfigType = models.IntegerField(null=True)  # 字典分类  (如 分类：1 )
    ConfigTypeNmae = models.CharField(max_length=120, null=True)  # 字典分类的名字  (如 分类名字：首页 )
    ConfigKeyNo = models.IntegerField(null=True)  # KeyID：1
    ConfigKeyName = models.CharField(max_length=120, null=True)  # KeyName：IndexColor
    ConfigKeyValue = models.CharField(max_length=120, null=True)  # KeyID：1
    ConfigFlag = models.BooleanField(default=True, null=True)
    ConfigCreatTime = models.DateField(default=False, null=True)

    class Meta:
        db_table = 'myapp_pageconfig'
        # verbose_name = '配置表s'
        verbose_name_plural = '配置表'


class Article(models.Model):
    ArticleID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    ArticleName = models.CharField(max_length=120, null=True)  # 文章名
    ArticleTime = models.DateField(null=True)  # 文章上传日期
    ArticleLikeCount = models.IntegerField(null=True, default=0)  # 文章点赞数
    ArticleReadCount = models.IntegerField(null=True, default=0)  # 文章阅读量
    ArticleAuthor = models.CharField(max_length=120, null=True)  # 文章作者
    ArticleDetail = models.TextField(max_length=1000, null=True)  # 文章内容
    ArticleIntroduc = models.CharField(max_length=220, null=True)  # 文章简介
    ArticleRemark = models.CharField(max_length=220, null=True)  # 备注
    ArticleType = models.IntegerField(null=True)  # 文章分类
    ArticleTypeName = models.CharField(max_length=120, null=True)  # 文章分类名称
    ArticleCreateTime = models.DateField(null=True)

    class Meta:
        db_table = 'Article'


class Province(models.Model):
    ProvinceID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    ProvinceName = models.CharField(max_length=120, null=True)  # 省份名

    class Meta:
        db_table = 'Province'


class City(models.Model):
    CityID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    CityName = models.CharField(max_length=120, null=True)  # 城市名
    ProvinceID = models.ForeignKey(Province, null=True, on_delete=models.SET_NULL)  # 省份ID
    IsCapitalCity = models.IntegerField(null=True, default=0)  # 是否省会城市 0：否 1：是

    class Meta:
        db_table = 'City'


class District(models.Model):
    DistrictID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    DistrictName = models.CharField(max_length=120, null=True)  # 城市名
    ProvinceID = models.ForeignKey(Province, null=True, on_delete=models.SET_NULL)  # 省份ID
    CityID = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)  # 市ID

    class Meta:
        db_table = 'District'


class Good(models.Model):
    GoodID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    GoodType = models.IntegerField(null=True)  # 商品分类
    GoodTypeName = models.CharField(max_length=120, null=True)  # 商品分类名称
    GoodSaleType = models.IntegerField(null=True)  # 商品销售类型
    GoodHotSale = models.IntegerField(default=0,null=True)  # 热销类型  1为热销类型
    GoodSaleTypeName = models.CharField(max_length=120, null=True)  # 商品销售类型名称
    GoodName = models.CharField(max_length=120, null=True)  # 商品名字
    GoodSubtitle = models.CharField(max_length=120, null=True)  # 商品销售名称
    GoodCharac = models.CharField(max_length=120, null=True)  # 商品特性e
    GoodIntroduct = models.CharField(max_length=220, null=True)  # 商品简介
    GoodOrigiPrice = models.CharField(max_length=120, null=True)  # 商品原价
    GoodSaleCount = models.IntegerField(null=True, default=0)  # 销量
    GoodSalePrice = models.CharField(max_length=120, null=True)  # 销售价
    GoodDiscount = models.CharField(max_length=120, null=True)  # 折头
    GoodDetail = models.TextField(max_length=1120, null=True)  # 详情
    GoodInstockCount = models.IntegerField(default=0, null=True)  # 商品库存
    GoodLikeCount = models.IntegerField(default=0, null=True)  # 点赞数
    GoodSaveCount = models.IntegerField(default=0, null=True)  # 收藏数
    GoodVipPoint = models.IntegerField(default=0, null=True)  # 商品积分
    GoodRemark = models.CharField(max_length=220, null=True)  #
    GoodCreateTime = models.DateField(max_length=120, null=True)  #

    class Meta:
        db_table = 'Good'


class Say(models.Model):
    SayID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    SayType = models.IntegerField(default=0, null=True)  # 评论类型 0:默认好评 1差评 2中 三差评
    SayTypeName = models.CharField(max_length=12, null=True)  # 评论类型 0:默认好评 1差评 2中 三差评
    SayDetail = models.TextField(max_length=1002, null=True)  # 评论详情
    SayRemark = models.CharField(max_length=112, null=True)  # 备注
    SayCreateTime = models.DateField(null=True)  # 操作时间
    Say_GoodID = models.ForeignKey(Good, null=True, on_delete=models.SET_NULL)  # 1对多外键

    class Meta:
        db_table = 'Say'


class GoodUrl(models.Model):
    GUrlID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    GUrlUrl = models.CharField(max_length=220, null=True)  # 图片地址
    GUrlMain = models.IntegerField(default=0, null=True)  # 是否主图 1:是，0否
    GUrlRemark = models.CharField(max_length=112, null=True)  # 备注
    GUrlCreateTime = models.DateField(max_length=12, null=True)  # 操作时间
    GUrl_GoodID = models.ForeignKey(Good, null=True, on_delete=models.SET_NULL)  # 1对多外键

    class Meta:
        db_table = 'GoodUrl'


class GoodStyle(models.Model):
    GStyleID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    GStyleType = models.IntegerField(null=True)  # 款式类型
    GStyleTypeName = models.CharField(max_length=112, null=True)  # 款式类型名字
    GStyleDetail = models.CharField(max_length=112, null=True)  # 款式详情
    GStyleRemark = models.CharField(max_length=212, null=True)  # 操作时间
    GStyleCreateTime = models.DateField(null=True)
    GStyle_GoodID = models.ManyToManyField(Good, through='GoodGoodStyleRela')

    # 与商品多对多 通过ManyToManyField  django会自动生成 多对多关系自动生成的关系表，但是如果想额外增加字段，或者说与现有的系统集成，这个关系表已经存在了，那对于这样的情形，Django允许指定一个用于管理多对多关系的中间模型，然后就可以把这些额外的字段添加到这个中间模型中，

    class Meta:
        db_table = 'GoodStyle'


class GoodGoodStyleRela(models.Model):
    GGSGoodGStyleID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    GGSGoodID = models.ForeignKey(Good, on_delete=models.DO_NOTHING, null=True)  # 商品ID外键
    GGSGStyleID = models.ForeignKey(GoodStyle, on_delete=models.DO_NOTHING, null=True)  # 款式ID外键
    GGSRemark = models.CharField(max_length=112, null=True)  # 备注
    GGSCreateTime = models.DateField(null=True)

    class Meta:
        db_table = 'GoodGoodStyleRela'


class Guest(models.Model):
    GuestID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    GuestType = models.IntegerField(null=True)  # 客人类型
    GuestTypeName = models.CharField(null=True, max_length=40)  # 客人分类名称
    GuestDocType = models.IntegerField(null=True)  # 证件号码类型
    GuestDocTypeName = models.CharField(null=True, max_length=20)  # 证件号码类型名字
    GuestDocNo = models.CharField(null=True, max_length=40)  # 证件号码
    GuestDocName = models.CharField(null=True, max_length=40)  # 证件姓名
    GuestName = models.CharField(null=True, max_length=140)  # 姓名
    GuestBornDate = models.DateField(null=True, max_length=40)  # 出生日期
    GuestSex = models.IntegerField(null=True, default=0)  # 性别  0:男 1 女  2 未知
    GuestNativePlace = models.CharField(null=True, max_length=40)  # 籍贯
    GuestNation = models.CharField(null=True, max_length=40)  # 民族
    GuestStatus = models.CharField(null=True, max_length=40)  # 客人状态
    GuestResAddress = models.CharField(null=True, max_length=140)  # 户籍地址
    GuestPhotoURL = models.CharField(null=True, max_length=240)  # 头像照片地址
    GuestRemark = models.CharField(null=True, max_length=140)  # 备注
    GuestMoney = models.CharField(max_length=120, null=True)  # 账户余额
    GuestCreateTime = models.DateField(null=True)  # 新建时间

    class Meta:
        db_table = 'Guest'


class Vip(models.Model):
    VipID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    VipType = models.IntegerField(default=0, null=True)  # 会员等级
    VipiTypeName = models.CharField(max_length=120, null=True)  # 会员等级
    VipPoint = models.IntegerField(default=0, null=True)  # 会员等级分值
    VipRemark = models.CharField(max_length=120, null=True)  # 备注
    ViprCreateTime = models.DateField(null=True)  #
    Guest_VipID = models.ForeignKey(Guest, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'Vip'


class GuestReceAddress(models.Model):
    GReceID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    GReceAddress = models.CharField(max_length=222, null=True)  # 快递地址
    GReceTel = models.CharField(max_length=220, null=True)  # 收快递电话
    GReceIsDefult = models.IntegerField(default=0, null=True)  # 是否默认 0 否
    GReceCityID = models.IntegerField(null=True)  # 城市ID
    GReceCityName = models.CharField(max_length=220, null=True)  # 城市名字
    GReceProvinceID = models.IntegerField(null=True)  # 省ID
    GReceProvinceName = models.CharField(max_length=220, null=True)  #
    GReceDistrictID = models.IntegerField(null=True)  # 区ID
    GReceDistrictName = models.CharField(max_length=220, null=True)  #
    GReceIsFlat = models.IntegerField(default=1, null=True)  # 是否有效  1 是
    GReceRemark = models.CharField(max_length=220, null=True)  #
    GReceCreateTime = models.DateField(null=True)  #
    GRece_GuestID = models.ForeignKey(Guest, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'GuestReceAddress'


class User(models.Model):
    UserID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    UserName = models.CharField(max_length=222, null=True)  # 用户名
    UsePassword = models.CharField(max_length=220, null=True)  # 密码
    UseTel = models.CharField(max_length=220, null=True)  # 联系方式
    UseState = models.IntegerField(null=True)  # 是否默认 0 否
    UseStateName = models.CharField(max_length=220, null=True)  # 状态名字
    UserDocNo = models.CharField(max_length=220, null=True)  # 用户证件号码
    UserDocType = models.IntegerField(default=1, null=True)  # 证件类型
    UserDocTypeName = models.CharField(max_length=220, null=True)  # 证件类型名称
    UserPost = models.CharField(max_length=220, null=True)  # 岗位
    UserCreateTime = models.DateField(null=True)  #
    UserRemark = models.CharField(null=True, max_length=123)

    class Meta:
        db_table = 'User'


class Shop(models.Model):
    ShopID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    ShopName = models.CharField(max_length=120, null=True)  # 店名
    ShopHeadUrl = models.CharField(max_length=120, null=True)  # 店铺头像
    ShopResponName = models.CharField(max_length=120, null=True)  # 店家负责人
    ShopResponDocNo = models.CharField(max_length=120, null=True)  # 证件号
    ShopResponDocType = models.IntegerField(null=True)  # 负责人证件类型
    ShopResponDocTypeName = models.CharField(max_length=120, null=True)  # 负责人证件类型名称
    ShopResponTel = models.CharField(max_length=120, null=True)  # 负责人电话
    ShopTel = models.CharField(max_length=120, null=True)  # 店家前台电话
    ShopPhone = models.CharField(max_length=120, null=True)  # 店家联系电话
    ShopIntroduct = models.CharField(max_length=120, null=True)  # 店家简介
    ShopNotice = models.TextField(max_length=1000, null=True)  # 店家公告
    ShopDetail = models.CharField(max_length=220, null=True)  # 店家详情
    ShopAddress = models.CharField(max_length=120, null=True)  # 店家地址
    ShopLongitude = models.CharField(max_length=120, null=True)  # 经度
    ShopLatitude = models.CharField(max_length=120, null=True)  # 维度
    ShopBusinessPermitNo = models.CharField(max_length=120, null=True)  # 经营许可证
    ShopBusinessPermitUrl = models.CharField(max_length=120, null=True)  # 经营许可证地址
    ShopHealthPermitNo = models.CharField(max_length=120, null=True)  # 卫生许可证
    ShopHealthPermiUrl = models.CharField(max_length=120, null=True)  #
    ShopRemark = models.CharField(max_length=120, null=True)  #
    ShopCreateTime = models.CharField(max_length=120, null=True)  #

    class Meta:
        db_table = 'Shop'


class Swiper(models.Model):
    SwiperID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    SwiperUrl = models.CharField(max_length=120, null=True)  # 图片地址
    SwiperType = models.IntegerField(null=True)  # 轮播类型
    SwiperTypeName = models.CharField(max_length=120, null=True)  # 省份名
    SwiperIsFlat = models.IntegerField(default=1, null=True)  # 是否有效 1 ：有效 0 无效
    SwiperCreateTime = models.DateField(null=True)  #

    class Meta:
        db_table = 'Swiper'


class Order(models.Model):
    OrderID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    OrderCode = models.CharField(max_length=120, null=True)  # 订单号
    OrderType = models.IntegerField(null=True)  # 订单类型
    OrderTypeName = models.CharField(max_length=120, null=True)  # 订单类型名称
    OrderAmount = models.CharField(max_length=120, null=True)  # 订单金额
    OrderPayAmount = models.CharField(max_length=120, null=True)  # 支付金额
    OrderPayTime = models.DateField(max_length=120, null=True)  # 支付时间
    OrderTradeNo = models.CharField(max_length=120, null=True)  # 交易订单号
    OrderCreateTime = models.DateField(max_length=120, null=True)  # 交易订单号创建时间
    OrderRemark = models.CharField(max_length=120, null=True)  # 订单号
    OrderDeliType = models.IntegerField(default=0, null=True)  # 快递方式 0自提，1快递
    OrderDeliCost = models.CharField(max_length=120, null=True)  # 快递费用
    OrderInCar = models.IntegerField(default=1, null=True)  # 是否购物车订单信息
    Order_GuestID = models.ForeignKey(Guest, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'Order'


class OrderStatus(models.Model):
    OStatusID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    OStatusType = models.IntegerField(null=True)  # 状态类型
    OStatusTypeName = models.CharField(max_length=120, null=True)  # 商品数量
    OStatusValue = models.CharField(max_length=120, null=True)  # 状态值
    OStatusRemark = models.CharField(max_length=120, null=True)  #
    OStatusCreatTime = models.DateField(max_length=120, null=True)  #
    OstatusDeliTime = models.DateField(max_length=120, null=True)  # 发货时间
    OstatusReceTime = models.DateField(max_length=120, null=True)  # 收货时间
    OStatus_OrderID = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'OrderStatus'


class OrderDetail(models.Model):
    ODetailID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    ODetailCode = models.CharField(max_length=120, null=True)  # 唯一订单号
    ODetailGoodCount = models.IntegerField(null=True)  # 商品数量
    ODetailOriginPrice = models.CharField(max_length=120, null=True)  # 商品原价
    ODetailSalePrice = models.CharField(max_length=120, null=True)  # 商品售价
    ODetailSaleAmount = models.CharField(max_length=120, null=True)  # 商品总售价
    ODetailRemark = models.CharField(max_length=120, null=True)  # 备注
    OrderCreateTime = models.DateField(max_length=120, null=True)  #
    ODetailr_OrderID = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    ODetail_GuestID = models.ForeignKey(Guest, null=True, on_delete=models.SET_NULL)
    ODetail_GoodID = models.ForeignKey(Good, null=True, on_delete=models.SET_NULL)
    ODetail_GStyleID = models.ForeignKey(GoodStyle, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'OrderDetail'


class Dict(models.Model):
    DictID = models.AutoField(primary_key=True, unique=True, auto_created=True)
    DitcType = models.IntegerField(null=True)  # 字典类型
    DitcTypeName = models.CharField(max_length=120, null=True)  # 字典类型名字
    DictNo = models.IntegerField(null=True)  # 状态值
    DictName = models.CharField(max_length=120, null=True)  #
    DictSort = models.IntegerField(null=True)  # 排序
    DictFlay = models.IntegerField(default=1, null=True)  # 1 有效
    DictCreateTime = models.DateField(null=True)  #

    class Meta:
        db_table = 'Dict'
