// 示例：
// { "state": 0, "msg": "数据获取成功", "data": "" }
// 返回值
// state:
// 200 成功
//   < 0	表示异常
//     - 20001 操作失败
//       - 20002 代码已存在
//         - 30001 无权限
//           - 30002 系统错误
//             - 30003 参数错误
//               - 30004 路径不存在
// msg:
// 返回成功 / 错误异常信息

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 获取轮播图(get)
// URL: /api/swiper
send = {}
Response = {
    'Code': number,
    'Msg': string,
    'Data': {
        'DataSet': [{}]
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 获取热销榜(GET)
// URL: /api/hot_sale
send = {
    'GoodSaleType': 1,
    'PageNo': number,
    'PageSize': number,
}
Response = {
    'Code': number,
    'Msg': string,
    'Data': {
        'PageNo': number,
        'PageSize': number,
        'RowCount': number,
        'DataSet': [{}]
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 获取首页商品列表(GET)
// URL: /api/good
send = {
    'PageNo': number,
    'PageSize': number,
},
    Response = {
        'Code': number,
        'Msg': string,
        'Data': {
            'PageNo': number,
            'PageSize': number,
            'RowCount': number,
            'DataSet': [{}]
        }
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 首页搜索框模糊查询(POST)
// URL: /api/search_good
send = {
    'PageNo': number,
    'PageSize': number,
    'search': string,
},
    Response = {
        'Code': number,
        'Msg': string,
        'Data': {
            'PageNo': number,
            'PageSize': number,
            'RowCount': number,
            'DataSet': [{}]
        }
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 店家信息(GET)
// URL: /api/shop
send = {},
    Response = {
        'Code': number,
        'Msg': string,
        'Data': {
            'DataSet': {}
        }
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 获取店家公告(GET)
// URL: /api/shop_notice
send = {},
    Response = {
        'Code': number,
        'Msg': string,
        'Data': {
            'DataSet': []
        }
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 获取销售类型不同的商品(首次加载, 不同销售类型的商品各加载15个)(GET)
// URL: /api/init_sale_type
send = {
    'PageNo': number,
    'PageSize': number,
    'GoodSaleType': number   // 默认0为全查询
},
    Response = {
        'Code': number,
        'Msg': string,
        'Data': {
            'PageNo': number,
            'PageSize': number,
            'RowCount': number,
            'DataSet': [{}]
        }
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 资讯文章(首次加载, 不同咨询文章5个)(GET)
// URL: /api/init_article
send = {
    'PageNo': number,
    'PageSize': number,
    'ArticleType': number   // 默认0为全查询
},
    Response = {
        'Code': number,
        'Msg': string,
        'Data': {
            'PageNo': number,
            'PageSize': number,
            'RowCount': number,
            'DataSet': [{}]
        }
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 获取用户资料(GET)
// URL: /api/guestinfo
send = {},
    Response = {
        'Code': number,
        'Msg': string,
        'Data': {
            'DataSet': {}
        }
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 订单列表(GET)
// URL: /api/order
send = {
    'PageNo': number,
    'PageSize': number,
    'OrderType': number     // 默认0为全查询
},
    Response = {
        'Code': number,
        'Msg': string,
        'Data': {
            'DataSet': [{}]
        }
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 个人信息修改(POST)
// URL: /api/change_guest_info
send = {
    'GuestSex': number,
    'GuestName': number,
    'GuestPhotoURL': string,
    'GuestRemark': string
},
    Response = {
        'Code': number,
        'Msg': string,
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 获取快递地址(GET)
// URL: /api/rece_address
send = {},
    Response = {
        'Code': number,
        'Msg': string,
        'Data': {
            'DataSet': [{}]
        }
    }

// 删除快递地址(GET)
// URL: /api/del_rece_address
send = {
    'GReceID': number,
},
    Response = {
        'Code': number,
        'Msg': string,
    }

//
// 新增快递地址(POST)
// URL: /api/add_rece_address
send = {
    'GReceAddress': string,
    'GReceTel': string,
    'GReceIsDefult': number,
    'GReceRemark': string,
},
    Response = {
        'Code': number,
        'Msg': string,
    }

// 新增快递地址(POST)
// URL: /api/change_rece_address
send = {
    'GReceID': number,
    'GReceAddress': string,
    'GReceTel': string,
    'GReceIsDefult': number,
    'GReceRemark': string,
},
    Response = {
        'Code': number,
        'Msg': string,
    }
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
