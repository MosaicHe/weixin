# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json

class KoovoxInterface:
	
	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.temp_root = os.path.join(self.app_root, 'templates')
		self.render = web.template.render(self.temp_root)
		
	def GET(self):
		return self.render.koovox()
		
	def POST(self):
		data = web.input()
		obj = data.obj
		action = data.action
		
		return ''

