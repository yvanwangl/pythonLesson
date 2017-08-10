#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from hello import application

http_server = make_server('', 8080, application)
print('Server on port 8080...')
http_server.serve_forever()
