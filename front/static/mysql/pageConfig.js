// class PageConfig(models.Model):
//     ConfigID = models.IntegerField(primary_key=True, unique=True, auto_created=True)
//     ConfigDataType = models.IntegerField(null=True)  # 数据分类  (如 分类：1 数组 )
//     ConfigType = models.IntegerField(null=True)  # 字典分类  (如 分类：1 )
//     ConfigTypeNmae = models.CharField(max_length=120, null=True)  # 字典分类的名字  (如 分类名字：首页 )
//     ConfigKeyNo = models.IntegerField(null=True)  # KeyID：1
//     ConfigKeyName = models.CharField(max_length=120, null=True)  # KeyName：IndexColor
//     ConfigKeyValue = models.CharField(max_length=120, null=True)  # KeyID：1
//     ConfigFlag = models.BooleanField(default=True, null=True)
//     ConfigCreatTime = models.DateField(default=False, null=True)