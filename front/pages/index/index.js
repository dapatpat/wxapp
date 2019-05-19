//index.js
//获取应用实例
const app = getApp()
import aipPath from '../../http/apiConfig.js'
import reqData from '../../http/aipMethod.js'
// import routers from './router/router.js'
// import routerM from './router/routerMethod.js'
import redis from '../../utils/redis.js'
import getPageConfStorage from '../../utils/getStoragePro.js'
import pageInitDatas from '../../utils/pageInitDatas.js'
Page({
  data: {
    IndexCol: redis.pageConfigDatas.IndexCol,
    pageStyle: pageInitDatas,
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    imgUrls: [
      'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640',
      'https://images.unsplash.com/photo-1551214012-84f95e060dee?w=640',
      'https://images.unsplash.com/photo-1551446591-142875a901a1?w=640'
    ],
    col: [{
        'colName': '校园业务',
        'colUrl': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      },
      {
        'colName': '欧美激情',
        'colUrl': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      }, {
        'colName': '古典文学',
        'colUrl': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      }, {
        'colName': '校园业务',
        'colUrl': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      }, {
        'colName': '五月天',
        'colUrl': 'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640'
      },
    ]
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function() {
    // 判断是否有缓存，如有则取，并赋值全局变量；无则发起请求
    getPageConfStorage('pageConfigDatas').then(r => {
      this.setData({
        pageStyle: r.data,
        IndexCol: r.data.IndexCol
      })
      app.globalData.pageStyle = r.data
    }, r => {
      // 请求，如成功则用后端数据，并赋值全局变量；失败则读取前端初始化文件，并赋值全局变量
      app.globalData.reqData.httpPromise(aipPath.getPageConfig).then(res => {
        if (res.statusCode === 200) {
          redis.pageConfigInit(res.data.data);
          this.setData({
            pageStyle: redis.pageConfigDatas,
            IndexCol: redis.pageConfigDatas.IndexCol
          })
          app.globalData.pageStyle = redis.pageConfigDatas
        } else {
          this.setData({
            pageStyle: pageInitDatas,
            IndexCol: pageInitDatas.IndexCol
          })
          app.globalData.pageStyle = pageInitDatas
        }
      }, err => {
        this.setData({
          pageStyle: pageInitDatas,
          IndexCol: pageInitDatas.IndexCol
        })
        app.globalData.pageStyle = pageInitDatas
      })
    })




    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
  durationChange(e) {
    this.setData({
      duration: e.detail.value
    })
  },
  goToGoodDT: function() {
    app.globalData.routerM.reTo(app.globalData.routers.goodDt, {})
  }
})