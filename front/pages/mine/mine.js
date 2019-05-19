// pages/mine/mine.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    imgUrls: [
      'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640',
      'https://images.unsplash.com/photo-1551214012-84f95e060dee?w=640',
      'https://images.unsplash.com/photo-1551446591-142875a901a1?w=640'
    ],

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    this.setData({
      pageStyle: app.globalData.pageStyle,
      MineOrderStatus: app.globalData.pageStyle.MineOrderStatus
    })

  },

  // 我的订单
  goToOrder: function() {
    app.globalData.routerM.reTo(app.globalData.routers.order, {})
  },

  // 我的个人信息设置
  goToGuestInfo: function() {
    app.globalData.routerM.reTo(app.globalData.routers.guestInfo, {})
  },

  // 我的收货地址
  goToAddress: function() {
    app.globalData.routerM.reTo(app.globalData.routers.address, {})
  }
})