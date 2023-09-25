// pages/results/results.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
      link:"",
      ilink:[{"_id":"63b9600be1a35c358c18483b","classname":"巨蟹座","icon":"/images/icon_eduye9epyqj/juxiezuo.png"},
      {"_id":"63b96087819ce84216575a3c","classname":"双子座","icon":"/images/icon_eduye9epyqj/shuangzizuo.png"},
      {"_id":"63b9609c819ce84216575d11","classname":"狮子座","icon":"/images/icon_eduye9epyqj/shizizuo.png"},
      {"_id":"63b960abf5cf3a165a3cb9db","classname":"处女座","icon":"/images/icon_eduye9epyqj/chunvzuo.png"},
      {"_id":"63b960bb819ce8421657614a","classname":"天秤座","icon":"/images/icon_eduye9epyqj/tianchengzuo.png"},
      {"_id":"63b960ebf5cf3a165a3cc27f","classname":"天蝎座","icon":"/images/icon_eduye9epyqj/tianxiezuo.png"},
      {"_id":"63b96101819ce84216576b1e","classname":"射手座","icon":"/images/icon_eduye9epyqj/sheshouzuo.png"},
      {"_id":"63b9611af5cf3a165a3cc88d","classname":"摩羯座","icon":"/images/icon_eduye9epyqj/mojiezuo.png"},
      {"_id":"63b9611af5cf3a165a3cc88c","classname":"水瓶座","icon":"/images/icon_eduye9epyqj/shuipingzuo.png"},
      {"_id":"63b9611af5cf3a165a3cc88f","classname":"双鱼座","icon":"/images/icon_eduye9epyqj/shuangyuzuo.png"},
      {"_id":"63b9611af5cf3a165a3cc88e","classname":"白羊座","icon":"/images/icon_eduye9epyqj/baiyangzuo.png"},
      {"_id":"63b9612af5cf3a165a3ccb43","classname":"金牛座","icon":"/images/icon_eduye9epyqj/jinniuzuo.png"}],
      sun:"",
      moon:"",
      rise:""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    this.setData({
      link : app.globalData.url,
      sun : app.globalData.sun,
      moon : app.globalData.moon,
      rise : app.globalData.rise,

    })
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