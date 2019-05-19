import Promise from '../utils/bulebird.js'
let getPageConfStorage = function (key){
  return new Promise ((res,rej)=>{
    wx.getStorage({
      key: key,
      success: r=>{
        res(r)
      },
      fail:r=>{
        rej(r)
      }
    })
  })
}

export default getPageConfStorage