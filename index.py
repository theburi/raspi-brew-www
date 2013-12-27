#!/usr/bin/env python
from cgi import escape
import sys, os
from flup.server.fcgi import WSGIServer


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    yield '<html>'
    yield '<h1>Brewing Master</h1>'
    yield '<table>'
    for k, v in sorted(environ.items()):
         yield '<tr><th>%s</th><td>%s</td></tr>' % (escape(k), escape(v))
    yield '</table>'
    yield '</html>'

WSGIServer(app).run()