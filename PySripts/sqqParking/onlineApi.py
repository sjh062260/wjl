#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年6月9日
# @author: jiaohui
import time,datetime,hashlib
from scpgSign import getNowTime,rightSign,sign
# import requests


# 全局参数定义

# 停车场
skey = "sqqParking"
# host = "http://wx.xxyxc.demo.shangquanquan.com"  # 停车缴费开发环境
host = "http://wx.yxc.scpretail.net"
# host = "http://wx.gdyxc.scpretail.net"
# skey = "scpgParking"
def sqq_car_in(carNo, startTime):
    carNo = carNo
    api = r'/parking/api/in'
    timestamp = getNowTime()
    # timestamp = '2017-04-19 15:48:57'
    # timestamp = '2017-03-22 10:58:15'
    # startTime = '2017-05-11 23:59:58'
    # timestamp = '2017-05-12 00:00:11'
    areaName = ''
    inPlace = '东桥头(进场通道1)'
    imageUrl = 'http://10.111.16.9:80/Capture_Images/20170511/浙HFB412/浙HFB412_20170511235958508.jpg'
    # imageUrl = 'http://www.tesla.cn/sites/default/files/images/referral/model-x--white.jpg'
    # imageUrl = ''
    # paramslist = ["carNo=" + carNo, "startTime=" + startTime, "timestamp=" + str(timestamp),"areaName="+areaName,"inPlace="+inPlace,"imageUrl="+imageUrl]
    paramslist = ["carNo=" + carNo, "startTime=" + startTime, "timestamp=" + timestamp,"areaName="+areaName,"inPlace="+inPlace,"imageUrl="+imageUrl]

    # paramslist = ["carNo=" + carNo, "startTime=" + startTime, "timestamp=" + str(timestamp)]

    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)

def sqq_car_out(carNo):
    carNo = carNo
    api = r'/parking/api/out'
    timestamp = getNowTime()
    # timestamp = '2016-11-28 15:57:36'
    # startTime = startTime
    outPlace = 'A出口'
    areaName = '一楼'
    imageUrl = 'http://10.111.16.9:80/Capture_Images/20170510/浙AF307V/浙AF307V_20170510123739102.jpg'
    # paramslist = ["carNo=" + carNo, "timestamp=" + str(timestamp),"outPlace="+outPlace]
    paramslist = ["carNo=" + carNo, "timestamp=" + str(timestamp),"outPlace="+outPlace,"areaName="+areaName,"imageUrl="+imageUrl]
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)


def sqq_force_out(carNo):
    carNo = carNo
    api = r'/parking/api/out'
    timestamp = getNowTime()
    outPlace = 'A出口'
    areaName = '一楼'
    imageUrl = 'http://www.tesla.cn/sites/default/files/images/referral/model-x--white.jpg'
    # timestamp = r'2017-02-15 14:10:21'
    paramslist = ["carNo=" + carNo, "timestamp=" + str(timestamp),"force="+"true","outPlace="+outPlace,"areaName="+areaName,"imageUrl="+imageUrl]
    # paramslist = ["carNo=" + carNo, "timestamp=" + '2016-09-09 18:59:18']
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)

def sqq_pay(carNo, startTime, money):
    carNo = carNo
    payWay = '6'
    api = r'/parking/api/pay'
    timestamp = getNowTime()
    # timestamp = '2016-10-05 18:24:39'
    startTime = startTime
    # payTime = '2017-05-24 18:10:00'
    payTime = timestamp
    money = money
    paramslist = ["startTime=" + startTime, "payTime=" + payTime, "money=" + str(money), "carNo=" + carNo,
                  "timestamp=" + str(timestamp),'payWay='+payWay]
    # paramslist = ["startTime=" + startTime, "payTime=" + payTime, "money=" + str(money), "carNo=" + carNo,
    #               "timestamp=" + str(timestamp)]
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)

def sqq_query_car(carNo):
    carNo = carNo
    api = r'/parking/api/query'
    timestamp = getNowTime()
    # timestamp = "2016-10-09 13:38:17"
    paramslist = ["carNo=" + carNo, "timestamp=" + str(timestamp)]
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)

if __name__ == "__main__":
    # carNo = r'陕AR06U3'
    payTime = getNowTime()
    # carNo = r'陕Asvr01'
    carNo = r'鄂A88888'
    startTime = r'2017-07-21 18:45:36'
    # startTime = r''
    # timestamp = r'2016-10-05 21:22:47'
    money = 0
    sqq_car_in(carNo,startTime)
    sqq_query_car(carNo)
    # sqq_pay(carNo,startTime,money)
    # sqq_car_out(carNo)
    sqq_force_out(carNo)


    # sign(tosign=sfsfsf,skey=sss)