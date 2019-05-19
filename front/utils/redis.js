import pageInitDatas from './pageInitDatas.js'
var pageConfigDatas = {
  'test': 'test redis',
}

// ------------------------------------------  初始化变量  --------------------------------------
// 初始化复杂数据结构收集器
function pageConfigInit(pageConfigData) {
  let arrConfigData = {}
  pageConfigData.forEach(i => {
    if (i.ConfigDataType == 1) {
      arrConfigData[i.ConfigTypeNmae] = []
    } else {
      pageConfigDatas[i.ConfigKeyName] = i.ConfigKeyValue // 简单对象设置
    }
  })
  pageConfigM(pageConfigData, arrConfigData)
}

// -------------------------------------  数据结构简单的字典数据进行缓存  ---------------------------
function pageConfigM(pageConfigData, arrConfigData) {
  pageConfigData.forEach(i => {
    // 数组类型
    if (i.ConfigDataType == 1) {
      arrConfigData[i.ConfigTypeNmae].push(i) //将栏目等数组类型的推到一个数组里面待处理
    }
  })
  // return arrConfigData
  changArrConfigData(arrConfigData)
}


function changArrConfigData(arrConfigData) {
  Object.keys(arrConfigData).forEach(function(key) {
    console.log(arrConfigData)
    let b = []
    arrConfigData[key].forEach(i => {
      let name = i.ConfigKeyName
      let value = i.ConfigKeyValue
      if (b.length == 0) {
        i[name] = value
        b.push(i)
      } else {
        let el = b.find(k => {
          return i.ConfigKeyNo == k.ConfigKeyNo
        })
        if(el !== undefined){
          el[name] = value
        }else{
          i[name] = value
          b.push(i)
        }
      }
    })
    pageConfigDatas[key] = b
  })
  wx.setStorage({
    key: 'pageConfigDatas',
    data: pageConfigDatas,
  })
}

//-----------------------------------  栏目等数组对象的遍历和整理 => 转化为全局变量  ---------------------------------
// function getArrConfigDataToPageConfigDatas(arrConfigData) {
//   debugger
//   Object.keys(arrConfigData).forEach(function(key) {
//     wx.getStorage({
//       key: key,
//       success: function(r) {
//         let b = []
//         r.data.forEach(i => {
//           let name = i.ConfigyKeyName
//           let value = i.ConfigKeyValue
//           if (b.length == 0) {
//             i[name] = value
//             b.push(i)
//           } else {
//             b.forEach(k => {
//               if (k.ConfigKeyNo != i.ConfigKeyNo) {
//                 i[name] = value
//                 b.push(i)
//               } else {
//                 k[name] = value //不应该再用i,应该用原来的 item
//               }
//             })
//           }
//         })
//         pageConfigDatas[key] = b

//       }
//     })
//   })
//   return pageConfigDatas
// }


// // ------------------------------------------  初始化变量  --------------------------------------
//   // 初始化复杂数据结构收集器
// function pageConfigInit(pageConfigData){
//   let arrConfigData = {}
//   pageConfigData.forEach(i=>{
//     if(i.ConfigDataType==1){
//       arrConfigData[i.ConfigTypeNmae] =[]
//     }
//   })
//   return arrConfigData
// }

// // -------------------------------------  数据结构简单的字典数据进行缓存  ---------------------------
// function pageConfigM(pageConfigData, arrConfigData) {
//   pageConfigData.forEach(i => {
//     // 数组类型
//     if (i.ConfigDataType == 1) {
//       arrConfigData[i.ConfigTypeNmae].push(i) //将栏目等数组类型的推到一个数组里面待处理
//     } else {
//       wx.setStorage({
//         key: i.ConfigTypeNmae,
//         data: i
//       })
//     }
//     wx.getStorage({             //  数据结构简单的字典数据 => 赋值给全局变量 
//       key: i.ConfigTypeNmae,
//       success(res) {
//         pageConfigDatas[i.ConfigTypeNmae] = res.data
//       }
//     })
//   })
//   setArrayConfigData(arrConfigData)
//   getArrConfigDataToPageConfigDatas(arrConfigData)
// }

// // -----------------------------------  数据结构复杂的字典数据进行缓存  ---------------------------------
// function setArrayConfigData(arrConfigData){
//   Object.keys(arrConfigData).forEach(function (key) {
//     wx.setStorage({
//       key:key,
//       data: arrConfigData[key]
//     })
//   })
// }


// //-----------------------------------  栏目等数组对象的遍历和整理 => 转化为全局变量  ---------------------------------
// function getArrConfigDataToPageConfigDatas(arrConfigData){
//   Object.keys(arrConfigData).forEach(function (key) {
//     wx.getStorage({
//       key: key,
//       success:function(r){
//         let b =[]
//         r.data.forEach(i=>{
//           let name = i.ConfigyKeyName
//           let value = i.ConfigKeyValue
//           if (b.length == 0){
//             i[name] = value
//             b.push(i)
//           }else{
//             b.forEach(k=>{
//               if(k.ConfigKeyNo != i.ConfigKeyNo){
//                 i[name] = value
//                 b.push(i)
//               }else{
//                 k[name] = value   //不应该再用i,应该用原来的 item
//               }
//             })
//           }
//         })
//         pageConfigDatas[key] = b

//       }
//     })
//   })
//   return pageConfigDatas
// }


let pageConfig = {
  'pageConfigM': pageConfigM,
  'pageConfigDatas': pageConfigDatas,
  'pageConfigInit': pageConfigInit
}

export default pageConfig