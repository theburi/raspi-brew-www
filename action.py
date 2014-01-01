#!/usr/bin/python
#todo:
#security
#use pi's kernel drivers instead of RPi.gpio

from flup.server.fcgi import WSGIServer
import sys, urlparse

ActionPipeName = '/tmp/ActionPipeName'

def VerifyAction(actionId):

    if os.path.exists(ActionPipeName):
            with open(ActionPipeName, "r") as output_file:

                for line in output_file:
                    [text, action, a_id] = line.split(";")
                    if a_id == int(i["action"]):
                        return True
    return False

def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    i = urlparse.parse_qs(environ["QUERY_STRING"])
    # useful because flup is expecting a string to be returned
    yield ('&nbsp;')


    if "action" in i:
        if VerifyAction(int(i["action"])):
            open(ActionPipeName, "w").close()





WSGIServer(app).run()
