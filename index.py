#!/usr/bin/env python
from cgi import escape
import sys, os
from flup.server.fcgi import WSGIServer

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, ParseError
from xml.etree.ElementTree import SubElement


ActionPipeName = '/tmp/ActionPipeName'


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    yield '<html><head>'
    #yield '<script src=\"prototype.js\"></script> '
    yield '<script src=\"http://ajax.googleapis.com/ajax/libs/prototype/1.7.1.0/prototype.js\"></script>'

    yield '</head><body>'

    yield '<script type=\"text/javascript\">\n function go(command) { new Ajax.Request(\'/action.py?action=\''
    yield '+ command , \n { onSuccess: success, onFailed: failed, method: \'GET\'}  ); $(\'log\').innerHTML += \' = success <br>\';}\n'
    yield 'function success(result) { $(\'log\').innerHTML += \' = success <br>\'; }\n'
    yield 'function failed(result) { $(\'log\').innerHTML += \' = failed <br>\'; }\n </script>'

    yield '<h1>Brewing Master</h1>'
    yield ''
    try:

        document = ElementTree.parse('/tmp/brewState.xml')
        yield 'reading file'
        root = document.getroot()
        yield root[0].tag
        for step in root.iter('step'):
            isActive = int(step.attrib['status'])
            if isActive == 255:
                yield '<div style=\'color:grey\'> %s - %s </div>' % (step.attrib['name'], step.attrib['status'])

            else:
                yield '<div style=\'color:black\'> %s - %s </div>' % (step.attrib['name'], step.attrib['status'])
                yield '<div style=\'margin-left:20px;\'> %s - %s </div>' % (root[1].tag, root[1].text)
                yield '<div style=\'margin-left:20px;\'> %s - %s </div>' % (root[2].tag, root[2].text)

                output_file = ''
                if os.path.exists(ActionPipeName):
                    output_file = open(ActionPipeName, "r")

                    for line in output_file:
                        if len(line) > 3:
                            [text, action, a_id] = line.split(";")
                            yield '%s  %s' % (action, a_id)
                            yield "<input type=\"button\" value=\"%s\" onclick=\"go(\'%s\')\">" % (
                                action, a_id.rstrip())

        yield '<div id=\"log\">Log Entries go here<br></div>'
        yield '</body></html>'

    except ParseError as pe:
        yield '<p> %s <p> %s' % (pe.message, pe.text)
    except Exception as e:
        yield '<p> %s' % e.message


WSGIServer(app).run()