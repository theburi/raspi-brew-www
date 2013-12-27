#!/usr/bin/env python
from cgi import escape
import sys, os
from flup.server.fcgi import WSGIServer

from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    yield '<html><body>'
    yield '<h1>Brewing Master</h1>'
    yield ''
    try:

        document = ElementTree.parse('/tmp/brewState.xml')
        yield ElementTree.tostring(document)
        root = document.getroot()
        for child in root:
            yield child.tag, child.attrib

        yield '<table>'

        for k, v in sorted(environ.items()):
            yield '<tr><th>%s</th><td>%s</td></tr>' % (escape(k), escape(v))
        yield '</table>'
        yield '</body></html>'

    except:
        yield '<b>%s</b></br>' % sys.exc_info()[0]



WSGIServer(app).run()