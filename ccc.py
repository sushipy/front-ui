# coding: UTF-8
import sys
import json
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import EventDAO
import urlparse
import createHTML

class JsonResponseHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        print "POST"

        parsed_path = urlparse.urlparse(self.path)
        print parsed_path.path

        if 'create' in parsed_path.path:
            content_len = int(self.headers.get('content-length'))
            requestBody = self.rfile.read(content_len).decode('UTF-8')
            eList = json.loads(requestBody)

            date = eList['date'].encode('utf-8')
            ftime = eList['ftime'].encode('utf-8')
            time = eList['time'].encode('utf-8')
            title = eList['title'].encode('utf-8')
            room = eList['room'].encode('utf-8')
            promotor_name = eList['promotor_name'].encode('utf-8')
            promotor_email = eList['promotor_email'].encode('utf-8')
            capacity = eList['capacity'].encode('utf-8')
            descri = eList['descri'].encode('utf-8')
            agenda = eList['agenda'].encode('utf-8')
            note = eList['note'].encode('utf-8')
        
            event = EventDAO.Event()
            queryarray = [date, ftime, time, title, room, promotor_name, promotor_email, capacity, descri, agenda, note]
            print "soga"
            event.create(queryarray)
            print "create"
            self.send_response(200)
            self.end_headers()
            print "Create OK"
        elif 'events' in parsed_path.path:
            content_len = int(self.headers.get('content-length'))
            requestBody = self.rfile.read(content_len).decode('UTF-8')
            eList = json.loads(requestBody)

            event_id = eList['event_id']
            promotor_email = eList['promotor_email']

            evid = int(event_id)

            event = EventDAO.Event()
            event.participate(evid,promotor_email)
            self.send_response(200)
            self.end_headers()
            print "Sanka OK"

    def do_GET(self):
        print "GET"

        event = EventDAO.Event()
        eventlist = event.find_event_all()
        cnt = len(eventlist)

        parsed_path = urlparse.urlparse(self.path)
        print parsed_path.path

        if 'showlist' in parsed_path.path:
            print "showlist"

            makeHTML = createHTML.createHTML()
            res = makeHTML.showlistHTML(cnt,eventlist)

            self.send_response(200)
            self.send_header('Content-type', 'text/html;charset=utf-8')
            self.end_headers()
            self.wfile.write(res)
        elif 'events' in parsed_path.path:
           print "detail"

           eventID = parsed_path.path[8:]
           makeHTML = createHTML.createHTML()
           res = makeHTML.detailHTML(eventID,eventlist)

           self.send_response(200)
           self.send_header('Content-type', 'text/html;charset=utf-8')
           self.end_headers()
           self.wfile.write(res)

    def do_PUT(self):
        print "PUT"

        parsed_path = urlparse.urlparse(self.path)
        print parsed_path.path

        if parsed_path.path.find(''):
            print "madamada"

        elif parsed_path.path.find(''):
            print "madamada"

    def do_DELETE(self):
        print "DELETE"

        parsed_path = urlparse.urlparse(self.path)
        print parsed_path.path

        if parsed_path.path.find(''):
            print "madamada"
        elif parsed_path.path.find(''):
            print "madamada"

if __name__ == '__main__':
    server = HTTPServer(('', 8001), JsonResponseHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
