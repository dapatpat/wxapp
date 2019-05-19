// class Dict(models.Model):
//     DictID = models.IntegerField(primary_key=True, unique=True, auto_created=True)
//     DitcType = models.IntegerField(null=True)  # 字典类型
//     DitcTypeName = models.CharField(max_length=120, null=True)  # 字典类型名字
//     DictNo = models.IntegerField(null=True)  # 状态值
//     DictName = models.CharField(max_length=120, null=True)  #
//     DictValue = models.DateField(max_length=120, null=True)  #
//     DictSort = models.IntegerField(null=True)  # 排序
//     DictFlay = models.IntegerField(default=1, null=True)  # 1 有效
//     DictCreateTime = models.DateField(max_length=120, null=True)  # 收货时间