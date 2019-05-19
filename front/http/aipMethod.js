import Promise from '../utils/bulebird.js'

// ---------------------------------------------------   异步  ---------------------------------------
let http = function(url, success, data = {}, method = 'get', fail) {
  if (method === 'post') {
    wx.request({
      url: url,
      data: data,
      method: 'POST',
      header: {
        'content-type': 'application/json' // 默认值
      },
      success,
      fail
    })
  } else {
    if (JSON.stringify(data) !== '{}') {
      let strParams = ''
      Object.keys(data).forEach(
        function(key) {
          strParams += '&' + key + '=' + data[key]
        }
      )
      url = url + '?' + strParams.substr(1)
    }
    wx.request({
      url: url,
      method: 'GET',
      header: {
        'content-type': 'application/json' // 默认值
      },
      success: success,
      fail
    })
  }
}

// ---------------------------------------------------     ---------------------------------------

let httpPromise = function(url, data = {}, method = 'get') {
  return new Promise(function(res, rej) {
    if (method === 'post') {
      wx.request({
        url: url,
        data: data,
        method: 'POST',
        header: {
          'content-type': 'application/json' // 默认值
        },
        success: function(re) {
          res(re)
        },
        fail: function(re) {
          rej(re)
        }
      })
    } else {
      if (JSON.stringify(data) !== '{}') {
        let strParams = ''
        Object.keys(data).forEach(
          function(key) {
            strParams += '&' + key + '=' + data[key]
          }
        )
        url = url + '?' + strParams.substr(1)
      }
      wx.request({
        url: url,
        method: 'GET',
        header: {
          'content-type': 'application/json' // 默认值
        },
        success: function(re) {
          res(re)
        },
        fail: function(re) {
          rej(re)
        }
      })
    }
  })
}

let reqData={
  'http':http,
  'httpPromise': httpPromise
}

export default reqData