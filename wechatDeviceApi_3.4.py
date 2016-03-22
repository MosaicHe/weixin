# qq_oauth

import urllib.request as req
import urllib.parse as parse
import json

APPID = 'wxc32d7686c0827f2a'
APPSECRET = '1981cab986e85ea0aa8e6c13fa2ea59d'
TOKEN = 'token'


AccessTokenUrl = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(APPID, APPSECRET)
AuthorizeUrl = 'https://api.weixin.qq.com/device/authorize_device?access_token=ACCESS_TOKEN'
CreateQrcode = 'https://api.weixin.qq.com/device/create_qrcode?access_token=ACCESS_TOKEN'
TransMsgUrl = 'https://api.weixin.qq.com/device/transmsg?access_token=ACCESS_TOKEN'

#dmenu = {"button":[{"type":"click","name":"koovox","key":"V1001_TODAY_MUSIC"},{"name":"菜单","sub_button":[{"type":"view","name":"智能耳机","url":"http://hpython.sinaapp.com/koovox"},{"type":"view","name":"智能路由","url": "http://v.qq.com/"},{"type":"click","name":"意见反馈","key":"V1001_GOOD"}]},{"type":"click","name":"我","key":"ME"}]}
dmenu = {"button":[{"type":"click","name":"点灯","key":"V1001_LIGHT_ON"},{"type":"click","name":"灭灯","key":"V1002_LIGHT_OFF"}]}

    
def createMenu(token, menu):
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' %token
    data = menu
    data = json.dumps(data,ensure_ascii=False)
    request = req.Request(url, method='POST')
    request.add_header('Content-Type', 'application/json')
    request.add_header('encoding', 'utf-8')
	
    response = req.urlopen(request, parse.unquote_to_bytes(data))
    result = response.read()
    print(result)
    return result
	
def getAccessToken(url):
    rsp = req.urlopen(url)
    token = rsp.read().decode('utf-8')
    token = json.loads(token).get('access_token')
    print(token)
    return token
	
	
def deviceAuth(url):
    data = {"device_num":"1","device_list":\
            [{"id":"koovox_02", "mac":"00025b00ff02", \
              "connect_protocol":"3", "auth_key":"", \
              "close_strategy":"1", "conn_strategy":"1",\
              "crypt_method":"0", "auth_ver":"0", \
              "manu_mac_pos":"-1", "ser_mac_pos":"-2"}], "op_type":"0"}
    data = json.dumps(data,ensure_ascii=False)
    request = req.Request(url, method='POST')
    request.add_header('Content-Type', 'application/json')
    request.add_header('encoding', 'utf-8')
    response = req.urlopen(request, parse.unquote_to_bytes(data))
    result = response.read()
    print(result)
    return result

def createQrcode(url):
    data = {"device_num":"1", "device_id_list":["koovox_02"]}
    data = json.dumps(data, ensure_ascii=False)
    request = req.Request(url, method = 'POST')
    request.add_header('Content-Type', 'application/json')
    request.add_header('encoding', 'utf-8')
    response = req.urlopen(request, parse.unquote_to_bytes(data))
    result = response.read()
    print(result)
    return result
	
	
if __name__ == '__main__':
    access_token = getAccessToken(AccessTokenUrl)
    createMenu(access_token, dmenu)
    url = AuthorizeUrl.replace('ACCESS_TOKEN', access_token)
    result = deviceAuth(url)
    url = CreateQrcode.replace('ACCESS_TOKEN', access_token)
    result = createQrcode(url)
	
	
	
	
	

















