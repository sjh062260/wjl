#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年7月16日
# @author: jiaohui
import time,datetime,hashlib,os
import requests

# 全局参数定义
# 生产环境
# HOST = "http://posapi.scpretail.net/"   # openapi 正式环境
# partnerId = "e2ee6a949a03fab193091ed2b092e058"
# skey = "liandiPos"
# mcode = '898330260120001'
# posId = '58932101'
# mcode = '898330260120001'
# posId = '58932101'
# posType = 'liandipos'
# 测试环境
HOST = "http://openapi.dev.wanjianglong.net/"  # openapi开发环境
# partnerId = "26e44f5a104b0a79d6799da149454138"
# skey = "scpgpos"
# posType = 'wpos'
# mcode = '143112'
# posId = 'bfe4f64b'
# posType = 'liandipos'
# mcode = '182043'
# posId = 'f7c9567c'


# 升级
# HOST = "http://sa-third-api.dev.wanjianglong.net/"  # openapi开发环境
# HOST = "http://sa-third-api.sgtnt.scpretail.net/"
partnerId = "67e03ba7fc9664ba811d64d9c8a7fe6f"
skey = "liandiPos_hyxyc"
posType = 'wpos'
mcode = '156225'
posId = '50888498'
posType = 'liandipos'


TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


# 获取当前时间
def get_now_time ():
    nowTime = time.strftime (TIMEFORMAT)
    return nowTime

# 通过params 和signKey生成正确的sign
def right_sign (params):
    params = params
    params.sort ()
    paramsstring = ''
    for line in params:
        paramsstring = paramsstring + line + '&'
    signString = paramsstring + 'skey=' + skey
    # sign = hashlib.md5(signString.encode('utf-8')).hexdigest()
    sign = hashlib.md5(signString).hexdigest()
    signedString = paramsstring + 'sign=' + sign
    return signedString

def signString (params):
    params = params
    params.sort ()
    paramsstring = ''
    for line in params:
        paramsstring = paramsstring + line + '&'
    signString = paramsstring + 'skey=' + skey
    # sign = hashlib.md5(signString.encode('utf-8')).hexdigest()
    sign = hashlib.md5(signString).hexdigest()
    return sign

# 查询优惠卷
def queryTicketByMobile(mobile):
    # mobile = mobile
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId,  "posId=" + posId,"mcode="+mcode,"mobile="+mobile,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/queryTicketByMobile'
    print (HOST + url+'?' + signedString)

# 查询会员
def recognizeMember():
    # mobile = mobile
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId,  "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp),]
    signedString = right_sign (params)
    url = 'third/crm/recognizeMember'
    print (HOST + url+'?' + signedString)

# 劵详情
def tickInfo(tickNo):
    tickNo = tickNo
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "tickNo=" + tickNo, "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/tickInfo'
    print (HOST + url+'?' + signedString)


# 单独核销优惠卷
def expendCoupon(tickNo):
    tickNo = tickNo
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "tickNo=" + tickNo, "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/expendCoupon'
    print (HOST + url+'?' + signedString)


# 退款通知
def cancel(type,originalOrderNo,refundAmount):
    type = type
    originalOrderNo = originalOrderNo
    refundAmount = refundAmount
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "type=" + type,"originalOrderNo=" + originalOrderNo, "refundAmount=" + refundAmount,  "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/cancel'
    print (HOST + url+'?' + signedString)

# 提交订单
def submitOrder(order,tickNo,externalCoupons):
    tickNo = tickNo
    order = order
    externalCoupons = externalCoupons
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "tickNo=" + tickNo, "order="+order,"posId=" + posId,"mcode="+mcode,"externalCoupons="+externalCoupons,"timestamp=" + str (timestamp)]
    # params = ["posType=" + posType, "partnerId=" + partnerId, "tickNo=" + "", "order="+order,"posId=" + posId,"mcode="+mcode,"externalCoupons="+"","timestamp=" + str (timestamp)]
    sign = signString(params)
    signedString = right_sign (params)
    url = 'third/crm/submitOrder'
    print (HOST + url+'?' + signedString)
    playload = {"posType":posType,"partnerId":partnerId,"tickNo":tickNo,"order":order,"posId":posId,"mcode":mcode,"externalCoupons":externalCoupons,"timestamp":str (timestamp),"sign":sign}
    url = HOST + url
    r = requests.post(url,data=playload)
    print(r.content)

# 交易结果通知
def tradeNotify(orderNo,isSuccess,payMethod,terminalNo,buyerId,payAmount):
    orderNo = orderNo
    isSuccess = isSuccess
    payMethod = payMethod
    terminalNo = terminalNo
    buyerId = buyerId
    payAmount = payAmount
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "isSuccess=" + isSuccess,"payMethod="+ payMethod,"terminalNo="+terminalNo,"buyerId="+buyerId,"payAmount="+payAmount,"orderNo="+orderNo,"posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    sign = signString(params)
    url = 'third/crm/tradeNotify'
    print (HOST + url+'?' + signedString)
    playload = {"posType":posType,"partnerId":partnerId, "isSuccess":isSuccess,"payMethod":payMethod,"terminalNo":terminalNo,"buyerId":buyerId,"payAmount":payAmount,"orderNo":orderNo,"posId":posId,"mcode":mcode,"timestamp":str (timestamp),"sign":sign}
    url = HOST + url
    r = requests.get(url,params = playload)
    print(r.url)
    print(r.content)
    # r = requests.post(url,data=playload)
    # print(r.url)
    # print(r.content)

# 广告和二维码查询
def mktInfo(orderNo):
    orderNo = orderNo
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "orderNo=" + orderNo, "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/mktInfo'
    print (HOST + url+'?' + signedString)

# 域名查询
def getPreUrl():
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId,  "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/getPreUrl'
    print (HOST + url+'?' + signedString)



if __name__ == "__main__":
    # print(time.ctime())
    start = time.ctime()
    # queryTicketByMobile(mobile='18627169820')
    # tickInfo(tickNo= '9001255400808')
    # expendCoupon(tickNo='123331064687909')
    # recognizeMember()
    # 提交订单
    # tickNo = '["252683477547064"]'
    tickNo = '[]'
    order  = '{"totalFee":"9900","orderNo":"60001562250125","actTotalFee":"9900","memberId":"77811170103163210304293","telephone":"18627169820","couponDiscValue":"0","state":"1"}'
    # order  = '{"totalFee":"9900","orderNo":"60001562250204","actTotalFee":"9900","telephone":"18627169820","couponDiscValue":"0","state":"1","payMethod":"2"}'
    # order  = '{"totalFee":"10000","orderNo":"60001562250121","actTotalFee":"10000","couponDiscValue":"0","state":"1",memberId:"77811170103163210304293"}'
    # "totalFee":"9900",
    # externalCoupons = '[{"couponCode":"100146240","dealTitle":"麦当劳5元券","dealValue":500,"count":2,"totalValue":1000,"channel":1},{"couponCode":"100146241","dealTitle":"肯德基10优惠券","dealValue":1000,"count":1,"totalValue":1000,"channel":2}]'
    externalCoupons = '[]'
    # submitOrder(order,tickNo,externalCoupons)

    # 交易结果通知
    tradeNotify(orderNo='60001562250125',isSuccess='true',payAmount='5000',payMethod='3',terminalNo='133567',buyerId='77811170103163210304293')
    # for i in range(10):
    #     print get_now_time()
    #     tradeNotify(orderNo='60001562250129',isSuccess='true',payAmount='5000',payMethod='3',terminalNo='133567',buyerId='77811170103163210304293')

    # 退款参数
    type = '3'
    originalOrderNo = '2017072718270350888498'
    refundAmount = '102'

    cancel(type,originalOrderNo,refundAmount)
    # getPreUrl()
    # mktInfo(orderNo = '2017072510144150888498')
