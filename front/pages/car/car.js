// pages/car/car.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    a: false,
    shopItem: [{
        'ID': 1,
        'isChoice': false,
        'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      },
      {
        'ID': 2,
        'isChoice': false,
        'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      },
      {
        'ID': 3,
        'isChoice': true,
        'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      },
      {
        'ID': 4,
        'isChoice': false,
        'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      },
      {
        'ID': 5,
        'isChoice': false,
        'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      },
      {
        'ID': 6,
        'isChoice': false,
        'imgUrls': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      },
    ],
    imgUrls: [
      'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640',
      'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640',
      'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640',
    ],
    img:'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    this.setData({
      pageStyle: app.globalData.pageStyle,
      Article: app.globalData.pageStyle.Article
    })

  },
  carChoice: function(e) {
    let that = this
    this.data.shopItem.forEach(i => {
      if (i.ID == e.target.id) {
          i.isChoice = !i.isChoice
      }
    })
    this.setData({
      shopItem: that.data.shopItem
    })
  }
})