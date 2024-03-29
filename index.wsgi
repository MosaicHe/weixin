# coding: UTF-8
import os
 
import sae
import web

sae.add_vendor_dir('vendor')
 
from weixinInterface import WeixinInterface
from koovoxInterface import KoovoxInterface
 
urls = (
'/weixin','WeixinInterface',
'/koovox','KoovoxInterface'
)
 
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)
 
app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)