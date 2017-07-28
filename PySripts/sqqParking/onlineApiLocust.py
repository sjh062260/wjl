#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年6月9日
# @author: jiaohui
import time,datetime,hashlib
from scpgSign import getNowTime,rightSign
from locust import HttpLocust,TaskSet,task
# 获取当前时间
skey = "sqqParking"
host = "http://wx.xxyxc.demo.shangquanquan.com"  # 停车缴费开发环境

class SqqParkingTest(TaskSet):

    def parking_in(self,carNo,startTime):
        carNo = r'鄂A87878'
        # api = r'/parking1/api/in'
        timestamp = getNowTime()
        # timestamp = '2017-03-22 10:58:15'
        startTime = startTime
        areaName = 'A区'
        inPlace = '1入口'
        # imageUrl = 'D:\360极速浏览器下载\u=1077361296,2970178117&fm=23&gp=0'
        imageUrl = 'http://www.tesla.cn/sites/default/files/images/referral/model-x--white.jpg'
        # imageUrl = ''
        paramslist = ["carNo=" + carNo, "startTime=" + startTime, "timestamp=" + str(timestamp), "areaName=" + areaName,
                      "inPlace=" + inPlace, "imageUrl=" + imageUrl]
        signedString = rightSign(paramslist, skey)
        # print(host + api + "?" + signedString)
        response = self.client.get("/parking1/api/in",signedString)
        print "Response status code:", response.status_code





class WebsiteUser(HttpLocust):
    task_set = SqqParkingTest
    # skey = "sqqParking"
    host = "http://wx.xxyxc.demo.shangquanquan.com"  # 停车缴费开发环境
    min_wait = 5000
    max_wait = 9000
