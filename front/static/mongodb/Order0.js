// Order = {
//     "OrderID": number,
//     "OrderCode": string,  //订单号
//     "OrderType": number,  //订单类型---->字典表类型
//     "OrderTypeName": string,  //订单类型名称
//     "Order_GuestID": string,  //买家ID，外键
//     "OrderAmount": string,  //订单金额
//     "OrderPayAmount": string,  //支付金额
//     "OrderPayTime": string,  //支付时间
//     "OrderTradeNo": string,  //交易订单号
//     "OrderDeliType": string,  //快递方式---->字典表类型
//     "OrderDeliCost": string,  //快递费用
//     "OrderStatus":{
//         "OStatusID":number,
//         "OStatusType":number //  状态类型  如交易、支付、发货、快递、收货等状态 ---->字典表类型
//         "OStatusTypeName":string //  状态类型名字
//         "OStatusRemark":string //  状态值
//         "OStatusCreatTime":string //  状态类型名字
//         "OstatusDeliTime":string //  发货时间
//         "OstatusReceTime":string //  收货时间
//     }
//     "OrderDetail": [
//         {
//             "ODetailID": number // 订单详情ID
//             "ODetail_GoodID": number  // ---->与商品关联的外键
//             "ODetailGoodCount": number  //商品数量
//             "ODetailOriginPrice": string  //商品原价
//             "ODetailSalePrice": string  //商品售价
//             "ODetailSaleAmount": string  //商品总售价
//             "ODetailCreatTime": string  //商品总售价
//             "ODetailRemark": string  //商品总售价
//             "ODetail_GStyle": {
//                 "GStyleID": number,
//                 "GStyleType": number,   // 款式类型---->字典表类型
//                 "GStyleDetail": string  //款式详情
//                 "GStyleRemark": string  //款式类型名字
//                 "GStyleCreateTime": string  //款式类型名字
//             }

//         }
//     ]
//     "OrderRemark": string,  //订单号
//     "OrderCreateTime": string,  //订单号
// }