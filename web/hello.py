#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s</H1>' % (environ['PATH_INFO'][1:] or 'web')
    print(environ['PATH_INFO'])
    return [body.encode('utf-8')]
