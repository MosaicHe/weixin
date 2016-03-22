# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree
import base64
from WechatData import buildPackage
from wechatDeviceApi import *
from models import Userdevice


 
class WeixinInterface:
 
    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="token" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法        
 
        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
	
    def POST(self):
        str_xml = web.data() #获得post来的数据	
        xml = etree.fromstring(str_xml)#进行XML解析
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        response = MessageHnadleInterface(fromUser, toUser, msgType).handle(xml)
        return response


class MessageHnadleInterface:

    def __init__(self, fromUser, toUser, msgType):
        self.fromUser = fromUser
        self.toUser = toUser
        self.msgType = msgType
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        
    def handle(self, xml):    
        if self.msgType == 'text':
            content = xml.find("Content").text
            return self.render.reply_text(self.fromUser,self.toUser, int(time.time()), content)

        if self.msgType == 'event':
            event = xml.find("Event").text

            # 关注事件
            if event == 'subscribe':
                content = '欢迎关注酷蜗科技'
                return self.render.reply_text(self.fromUser,self.toUser, int(time.time()), content)
            elif event == 'CLICK':
                eventKey = xml.find("EventKey").text
                fromUserName=xml.find("FromUserName").text
                device=Userdevice.findone(fromUserName=fromUserName)
                deviceType=device.deviceType
                deviceId=device.deviceId
                openId=device.openId
                if eventKey == 'V1001_LIGHT_ON':
                    cmdId = int('0x2001', 16)
                    content = '点灯'
                else:
                    cmdId = int('0x2002', 16)
                    content = '灭灯'
                    
                message = buildPackage(cmdId, 10)
                transMsg(deviceType, deviceId, openId, message)   
                return self.render.reply_text(self.fromUser,self.toUser, int(time.time()), content)
            elif event == 'unsubscribe':
                fromUserName=xml.find("FromUserName").text
                Userdevice.where(fromUserName=fromUserName).delete().execute()
                

        if self.msgType == 'device_event':
            event = xml.find("Event").text
            deviceType=xml.find("DeviceType").text
            deviceId=xml.find("DeviceID").text
            openId=xml.find("OpenID").text
            fromUserName=xml.find("FromUserName").text
            dev=Userdevice.findone(openId=openId)
            # 绑定/解绑事件
            if event == 'bind':
                # 数据库增加一条记录
                if dev:
                    pass
                else:
                    Userdevice.create(deviceId=deviceId, deviceType=deviceType, openId=openId, fromUserName=fromUserName)
                
            else:
                # 数据库删除一条记录
                Userdevice.where(deviceId=deviceId).delete().execute()
                
            return ''

        if self.msgType == 'device_text':
            content = xml.find("Content").text
            data = base64.b64encode(content)

            
            
                
            
            
        
	
