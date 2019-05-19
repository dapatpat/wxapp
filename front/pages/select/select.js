// pages/select/select.js
const app = getApp()
const order = ['red', 'yellow', 'blue', 'green', 'red']
import redis from '../../utils/redis.js'
Page({

  /**
   * 页面的初始数据
   */
  data: {
    SelectedCol: 1,
    SelectCol: redis.pageConfigDatas.SelectCol,
    pageStyle: app.globalData,
    // 对应商品类型接口
    GoodTypeName: [{
        'ID': 1,
        'Name': '科幻'
      },
      {
        'ID': 2,
        'Name': '言情'
      },
      {
        'ID': 3,
        'Name': '武侠'
      },
    ],
    imgUrls: [
      'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640',
      'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
    ],
    // 根据商品类型接口 查出对应商品类型的数据详情
    goodsItems: [
      [{
          'goosName': '挪威的森林',
          'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
        },
        {
          'goosName': '流浪地球',
          'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
        },
        {
          'goosName': '钢铁侠',
          'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
        },
      ],
      [{
          'goosName': '三体',
          'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
        },
        {
          'goosName': '黑色森林',
          'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
        },
        {
          'goosName': '地球往事',
          'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
        },
      ],
      []
    ],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    let that = this
    // 跑马灯循环控制函数
    setInterval(function() {
      let newArray = that.fnChangeArrayFirstItem(that.data.a)
      that.setData({
        a: newArray
      })
    }, 30000000)
     // 样式初始化
    this.setData({
      pageStyle:app.globalData.pageStyle,
      SelectCol: app.globalData.pageStyle.SelectCol
    })
  },

  fnChangeArrayFirstItem: function(array) {
    let firstItem = array.shift();
    array.push(firstItem);
    return array
  },

  changeSelectedCol: function(e) {
    this.setData({
      SelectedCol: e.target.id,
    })
  },
  goToGoodDT: function() {
    app.globalData.routerM.reTo(app.globalData.routers.goodDt, {})
  }
})