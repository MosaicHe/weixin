# -*- coding: utf-8 -*-

import MySQLdb
from skylark import Database, Model, Field
from config import DB_HOST, DB_PORT, DB_USER, DB_PWD, DB

class Userdevice(Model):
    id = Field()
    deviceId = Field()
    deviceType = Field()
    openId = Field()
    fromUserName = Field()


Database.set_dbapi(MySQLdb)   
Database.config(host=DB_HOST, port=DB_PORT, db=DB, user=DB_USER, passwd=DB_PWD)

if __name__ == '__main__':
    user = Userdevice(deviceId='koovox_01', deviceType='wechat', openId='123456', fromUserName='joysoft')
    user.save()




