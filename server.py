# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:19:15 2018

@author: Administrator
server.py
"""

from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()
