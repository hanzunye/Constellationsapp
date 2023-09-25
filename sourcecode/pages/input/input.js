// pages/input/input.js

const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    day: "1990-01-01",
    city: ['广东省', '广州市', '海珠区'],
    time : "11:11",
    results:''
  },
  cch(e) {
    this.setData({
      city: e.detail.value
    })
  },
  onTap: function() {
    this.requestToPython();
  },
 
  requestToPython: function() {
      // 设置请求参数
      const requestData = {
        // 设置Python程序的URL
        // url: 'http://127.0.0.1:8000',
        // 设置请求的数据
        data: {
          day: this.data.day,
          city: this.data.city,
          time: this.data.time
        },
        // 设置请求的方法
        method: 'POST',
        // 设置请求成功的回调函数
        success: res => {
          // 请求成功的处理逻辑
          // res.data 包含了Python程序返回的数据
          console.log(res.data);
          app.globalData.sun = res.data.sun;
          app.globalData.rise = res.data.rise;
          app.globalData.moon = res.data.moon;
          app.globalData.url = res.data.url_pic;
       
        },
        // 设置请求失败的回调函数
        fail: (res) => {
          // 请求失败的处理逻辑
          console.log(res.errMsg);
        },
        // 设置请求结束的回调函数
        complete: (res) => {
          // 请求结束的处理逻辑
          wx.navigateTo({
            url: '/pages/results/results',
          })
        }
      };
  
      // 发起网络请求
      wx.request(requestData);
    },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})