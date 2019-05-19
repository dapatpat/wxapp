// pages/article/article.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    DictArticleColTextColor: '#ccc',
    DictArticledColTextColor: 'red',
    DictUnArticledColTextColor: '#ccc',
    SelectedCol: 1,
    // 对应商品类型接口
    ArticleTypeName: [{
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
    // 根据商品类型接口 查出对应商品类型的数据详情
    ArticleItems: [
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
  onLoad: function (options) {
    this.setData({
      pageStyle: app.globalData.pageStyle,
      Article: app.globalData.pageStyle.Article
    })
  },

  changeSelectedCol: function (e) {
    this.setData({
      SelectedCol: e.target.id,
    })
  }
})