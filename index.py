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
    # <membership/>
    membership = Element('membership')

    # <membership><users/>
    users = SubElement(membership, 'users')

    # <membership><users><user/>
    SubElement(users, 'user', name='john')
    SubElement(users, 'user', name='charles')
    SubElement(users, 'user', name='peter')

    # <membership><groups/>
    groups = SubElement(membership, 'groups')

    # <membership><groups><group/>
    group = SubElement(groups, 'group', name='users')

    # <membership><groups><group><user/>
    SubElement(group, 'user', name='john')
    SubElement(group, 'user', name='charles')

    # <membership><groups><group/>
    group = SubElement(groups, 'group', name='administrators')

    # <membership><groups><group><user/>
    SubElement(group, 'user', name='peter')
    try:

        output_file = open('membership.xml', 'w')
        output_file.write('<?xml version="1.0"?>')
        output_file.write(ElementTree.tostring(membership))
        output_file.close()

    except IOError as e:
        yield '<b>%s</b></br>' % e
    try:
        document = ElementTree.parse('membership.xml')
    except IOError as e:
        yield '<b>%s</b></br>' % e

    yield ElementTree.tostring(document)

    yield '<table>'
    for k, v in sorted(environ.items()):
        yield '<tr><th>%s</th><td>%s</td></tr>' % (escape(k), escape(v))
    yield '</table>'
    yield '</body></html>'


WSGIServer(app).run()