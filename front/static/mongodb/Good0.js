// Good={
//     "GoodID":number,
//     "GoodType":number, //商品分类---->字典表类型
//     "GoodTypeName":string,  //商品分类名称
//     "GoodSaleType":number,  //商品销售类型，热销等---->字典表类型
//     "GoodSaleTypeName":string,  //商品销售类型名称
//     "Good_Gstyle":{                        // 对应mysql外键，此处用内嵌模式
//         "GStyleID":number,
//         "GStyleType":number,   // 款式类型---->字典表类型
//         "GStyleDetail":string  //款式详情
//         "GStyleRemark":string  //款式类型名字
//         "GStyleCreateTime":string  //款式类型名字
//     },
//     "Good_Url":[
//         {"GUrlID":nunber,
//         "GUrlUrl":string,  // 图片地址
//         "GUrlMain":number,  // 是否主图 1 ：是  0：否
//         "GUrlCreateTime":string,  // 图片地址
//         "GUrlUrl":string,  // 图片地址
//          }
//     ]
//     "GoodName":string, // 商品名字
//     "GoodSubtitle":string, // 商品销售名称
//     "GoodCharac":string, // 商品特性
//     "GoodIntroduct":string, // 商品简介
//     "GoodOrigiPrice":string, // 商品原价
//     "GoodSaleCount":string, // 销量
//     "GoodSalePrice":string, // 销售价
//     "GoodDiscount":number, // 折头
//     "GoodDetail":string, // 详情
//     "GoodInstockCount":nunber, // 商品库存
//     "GoodLikeCount":nunber, // 点赞数
//     "GoodSaveCount":nunber, // 收藏数
//     "GoodVipPoint":nunber, // 商品积分
//     "GoodRemark":string, // 商品积分
//     "GoodCreateTime":string, // 商品积分
// }