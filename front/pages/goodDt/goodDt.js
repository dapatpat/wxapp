// pages/goodDt/goodDt.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    DictSelectColTextColor: '#ccc',
    DictSelectedColTextColor: 'red',
    DictUnSelectedColTextColor: '#ccc',
    SelectedCol: 1,
    toView: 'red',
    disabled: false,
    standardShow: true,
    imgUrls: [
      'https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=640',
      'https://images.unsplash.com/photo-1551214012-84f95e060dee?w=640',
      'https://images.unsplash.com/photo-1551446591-142875a901a1?w=640'
    ],

    GoodTypeName: [{
        'ID': 1,
        'Name': '详情'
      },
      {
        'ID': 2,
        'Name': '规格'
      },
      {
        'ID': 3,
        'Name': '评论'
      },
    ],
    GStyle: [{
      'GStyleTypeName': '大小',
      'GStyleType': [{
          'ID': 1,
          'GStyleType': 1,
          'GStyleTypeName': '大小',
          'GStyleTypeValue': 'big'
        },
        {
          'ID': 1,
          'GStyleType': 1,
          'GStyleTypeName': '大小',
          'GStyleTypeValue': 'middle'
        },
        {
          'ID': 1,
          'GStyleType': 1,
          'GStyleTypeName': '大小',
          'GStyleTypeValue': 'small'
        }
      ]
    }, {
      'GStyleTypeName': '款式',
      'GStyleType': [{
          'ID': 1,
          'GStyleType': 2,
          'GStyleTypeName': '款式',
          'GStyleTypeValue': 'big'
        },
        {
          'ID': 1,
          'GStyleType': 2,
          'GStyleTypeName': '款式',
          'GStyleTypeValue': 'middle'
        },
        {
          'ID': 1,
          'GStyleType': 2,
          'GStyleTypeName': '款式',
          'GStyleTypeValue': 'small'
        },
      ]
    }, {
      'GStyleTypeName': '颜色',
      'GStyleType': [{
          'ID': 1,
          'GStyleType': 3,
          'GStyleTypeName': '颜色',
          'GStyleTypeValue': 'red'
        },
        {
          'ID': 1,
          'GStyleType': 3,
          'GStyleTypeName': '颜色',
          'GStyleTypeValue': 'greed'
        },
        {
          'ID': 1,
          'GStyleType': 3,
          'GStyleTypeName': '颜色',
          'GStyleTypeValue': 'blue'
        },
      ],
    }],


  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {

  },

  changeSelectedCol: function(e) {
    this.setData({
      SelectedCol: e.target.id,
    })
  },
  car: function() {
    let v = this.data.standardShow ? false : true
    this.setData({
      standardShow: v
    })
  }

})