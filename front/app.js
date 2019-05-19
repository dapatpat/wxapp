//app.js
import aipPath from './http/apiConfig.js'
import reqData from './http/aipMethod.js'
import routers from './router/router.js'
import routerM from './router/routerMethod.js'
import redis from './utils/redis.js'
import pageInitDatas from './utils/pageInitDatas.js'
import regeneratorRuntime from './utils/regenerator-runtime/runtime.js'
App({
  onLaunch: function() {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
    // 获取用户信息
    wx.getSetting({
        success: res => {
          if (res.authSetting['scope.userInfo']) {
            // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
            wx.getUserInfo({
              success: res => {
                // 可以将 res 发送给后台解码出 unionId
                this.globalData.userInfo = res.userInfo

                // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
                // 所以此处加入 callback 以防止这种情况
                if (this.userInfoReadyCallback) {
                  this.userInfoReadyCallback(res)
                }
              }
            })
          }
        }
      })
  },
  globalData: {
    reqData: reqData,
    routers: routers,
    aipPath: aipPath,
    userInfo: null,
    routers: routers,
    routerM: routerM,
    pageStyle:{}
  }
})