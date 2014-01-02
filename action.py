#!/usr/bin/env python


from flup.server.fcgi import WSGIServer
import os
import sys, urlparse

ActionPipeName = '/tmp/ActionPipeName'


def VerifyAction(actionId):
    if os.path.exists(ActionPipeName):
        with open(ActionPipeName, "r") as output_file:

            for line in output_file:
                [text, action, a_id] = line.split(";")

                if int(a_id.rstrip()) == actionId:

                    return True

    return False


def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])

    i = urlparse.parse_qs(environ["QUERY_STRING"])

    # useful because flup is expecting a string to be returned
    yield ('&nbsp;')


    try:
        if "action" in i:

            if VerifyAction(int(i["action"][0])):
                open(ActionPipeName, "w").close()
                yield 'Action processes'
            else:
                yield "Action was not found"

    except Exception as e:
        yield '<p>Error: '
        yield '<p> %s <p> %s' % (e.message,  e)


WSGIServer(app).run()
