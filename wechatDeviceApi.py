# -*- coding: utf-8 -*-
# wechat device api

import urllib
import urllib2
import urlparse
import json
from WechatData import buildPackage
import time


APPID = 'wxc32d7686c0827f2a'
APPSECRET = '1981cab986e85ea0aa8e6c13fa2ea59d'
TOKEN = 'token'
gtoken = None
gtime = 0


AccessTokenUrl = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(APPID, APPSECRET)
AuthorizeUrl = 'https://api.weixin.qq.com/device/authorize_device?access_token=ACCESS_TOKEN'
CreateQrcode = 'https://api.weixin.qq.com/device/create_qrcode?access_token=ACCESS_TOKEN'
TransMsgUrl = 'https://api.weixin.qq.com/device/transmsg?access_token=ACCESS_TOKEN'
VerifyQrcodeUrl = 'https://api.weixin.qq.com/device/verify_qrcode?access_token=ACCESS_TOKEN'
CreateMenu = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN'
GetOpenIdUrl = 'https://api.weixin.qq.com/device/get_openid?access_token=ACCESS_TOKEN&device_type=DEVICE_TYPE&device_id=DEVICE_ID'

def httppost(url, data):
    request = urllib2.Request(url)
    request.add_header('Content-Type', 'application/json')
    request.add_header('encoding', 'utf-8')

    response = urllib2.urlopen(request, json.dumps(data,ensure_ascii=False))
    result = response.read()
    print result
    return result

def getAccessToken():
    Time = time.time()
    global gtime
    global gtoken
    if Time > gtime + 1800:
        rsp = urllib2.urlopen(AccessTokenUrl)
        token = rsp.read().decode('utf-8')
        token = json.loads(token).get('access_token')
        print 'token:' + token
        gtoken = token
        gtime = Time
    else:
        token = gtoken
    return token

def createMenu(menu):
    access_token = getAccessToken()
    url = CreateMenu.replace('ACCESS_TOKEN', access_token)
    httppost(url, menu)


def createQrcode(data):
    access_token = getAccessToken()
    url = CreateQrcode.replace('ACCESS_TOKEN', access_token)
    httppost(url, data)

def deviceAuth(data):
    access_token = getAccessToken()
    url = AuthorizeUrl.replace('ACCESS_TOKEN', access_token)
    httppost(url, data)

def transMsg(device_type, device_id, open_id, content):
    access_token = getAccessToken()
    data = {'device_type':device_type, 'device_id':device_id, 'open_id':open_id, 'content':content}
    url = TransMsgUrl.replace('ACCESS_TOKEN', access_token)
    httppost(url, data)

def getOpenId(device_type, device_id):
    access_token = getAccessToken()
    url = GetOpenIdUrl.replace('ACCESS_TOKEN', access_token)
    url = url.replace('DEVICE_TYPE', device_type)
    url = url.replace('DEVICE_ID', device_id)
    rsp = urllib2.urlopen(url)
    open_id = json.loads(rsp.read().decode('utf-8')).get('open_id')
    print open_id
    return open_id
    

    
if __name__ == '__main__':
    menu = {"button":[{"type":"click","name":"OPEN","key":"V1001_LIGHT_ON"},{"type":"view","name":"JUMP","url":"http://hpython.sinaapp.com/koovox"}]}
    createMenu(menu)
    authData = {"device_num":"1","device_list":\
            [{"id":"BDE_WEIXIN_TTM", "mac":"c4be8459052f", \
              "connect_protocol":"3", "auth_key":"", \
              "close_strategy":"1", "conn_strategy":"1",\
              "crypt_method":"0", "auth_ver":"0", \
              "manu_mac_pos":"-1", "ser_mac_pos":"-2"}], "op_type":"0"}
    #deviceAuth(authData)
    #qrcodeData = {"device_num":"1", "device_id_list":["BDE_WEIXIN_TTM"]}
    #createQrcode(qrcodeData)
    #open_id = getOpenId('gh_c7b14a6dffc8', 'koovox_01')
    
    #message = buildPackage(0x2001, 10) 
    #transMsg('gh_c7b14a6dffc8', 'koovox_01', open_id[0], message)
