let reTo = function(router, params = {}) {
  if (JSON.stringify(params) !== '{}') {
    let strParams = ''
    Object.keys(params).forEach(
      function(key) {
        strParams += '&' + key + '=' + params[key]
      }
    )
    router = router + '?' + strParams.substr(1)
  }

  wx.navigateTo({
    url: router
  })
}


// ----------------------------   保留当前页面的跳转 （最多10个）--------------------------------
let naTo = function(router, params = {}) {
  if (JSON.stringify(params) !== '{}') {
    let strParams = ''
    Object.keys(params).forEach(
      function(key) {
        strParams += '&' + key + '=' + params[key]
      }
    )
    router = router + '?' + strParams.substr(1)
  }
  wx.navigateTo({
    url: router
  })
}

let naBk = function(num) {
  wx.navigateBack({
    delta: num
  })
}

 let routerM = {
  'reTo': reTo,
  'naTo': naTo,
  'naBk': naBk
}
export default routerM