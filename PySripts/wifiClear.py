#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年7月16日
# @author: jiaohui
import time,datetime,hashlib,requests,os


def clearFreePortalFlag(wifihost,usermac):
    playload = {"usermac":usermac}
    api = "/portal/clearFreePortalFlag"
    url = wifihost +api
    r = requests.post(url,data=playload)
    # print(r)
    print(r.content)

def midwareOffLine(midwarehost,userip,basId):
    playload = {"userIp":userip,"basId":basId}
    api = "/offline"
    url = midwarehost +api
    r = requests.post(url,data=playload)
    r.encoding = 'GB1312'
    data = r.text
    print(data)

def clearFreeCredit(wifihost,usermac):
    playload = {"usermac":usermac}
    api = "/portal/clearFreeCredit"
    url = wifihost +api
    r = requests.post(url,data=playload)
    print(r.content)
    

if __name__ == "__main__":
    # wifihost = "http://wifi.bdcsgc.mallshow.net"80-71-7A-45-AA-91
    # midwarehost = "http://portal.midware.mallshow.net"
    # wifihost = "http://graywifi.mallshow.mallshow.net"
    # midwarehost = "http://grayportal.midware.mallshow.net"
    # huawei honor 6
    # usermac = '80-71-7A-45-AA-91'
    # userip = '172.16.200.85'
    # basId = "10101"
    # clearFreePortalFlag(wifihost="http://wifi.reco.mallshow.mallshow.net",usermac="80-71-7A-45-AA-91")
    # midwareOffLine(midwarehost="http://portal.reco.midware.mallshow.net",userip="172.16.200.159",basId="9001")
    # midwareOffLine(midwarehost="http://portal.midware.dev.wanjianglong.net", userip="172.16.200.244", basId="10101")
    # clearFreeCredit(wifihost="http://wifi.reco.mallshow.mallshow.net",usermac="80-71-7A-45-AA-91")

    clearFreePortalFlag(wifihost="http://wifi.wjl.dev.wanjianglong.net",usermac="80-71-7A-45-AA-91")
    # midwareOffLine(midwarehost="http://portal.midware.mallshow.net",userip="172.16.200.85",basId="9001")
    midwareOffLine(midwarehost="http://portal.midware.dev.wanjianglong.net", userip="172.16.200.85", basId="9001")
    clearFreeCredit(wifihost="http://wifi.wjl.dev.wanjianglong.net",usermac="172.16.200.85")