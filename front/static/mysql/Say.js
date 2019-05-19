// Name	Code	Data Type	Length	Precision	Primary	Foreign Key	Mandatory
// SayID(评论ID)	UserID	int(11)	11		TRUE	FALSE	TRUE
// SayType(评论类型 3 好评   2中评   1差评  0 默认好评)	UserCode	varchar(100)	100		FALSE	FALSE	FALSE
// SayDetail(评论详情)	Password	varchar(100)	100		FALSE	FALSE	FALSE
// SayRemark(备注)	Remark	varchar(100)	100		FALSE	FALSE	FALSE
// SayCreateTime(操作时间)	CreateTime	datetime			FALSE	FALSE	FALSE
// Say_GoodID (外键)	Say_GoodID (外键)	<Undefined>			FALSE	FALSE	FALSE