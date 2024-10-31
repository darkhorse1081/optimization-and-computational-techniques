# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:45:34 2022

@author: Bryan Ruddy
"""

# Python 3 server example
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

hostName = "localhost"
serverPort = 8000

class RadioHandler():
    def __init__(self):
        self.clients = {};
        self.messages = [];
        self.sequence = 0;
        
    def registerClient(self, id):
        self.clients[id] = self.sequence
        print('Added client with ID ' + str(id))
    
    def addToQueue(self, msg):
        self.messages.append(msg)
        print('Added ' + str(msg) + ' to queue in position ' + str(self.sequence))
        self.sequence += 1
        
    def readFromQueue(self, id):
        if id not in self.clients:
            print('Error, request from unregistered client')
            return b'XXXX'
        print('Request from client ' + str(id) + ' in position ' + str(self.clients[id]))
        if self.clients[id] == self.sequence:
            return None
        else:
            if self.sequence > 100:
                print('Pruning queue')
                self.sequence -= 50
                for i in self.clients:
                    if self.clients[i] < 50:
                        self.clients[i] = 0
                    else:
                        self.clients[i] -= 50
                self.messages[0:50] = []
            msg = self.messages[self.clients[id]]
            self.clients[id] += 1
            return msg
radio = RadioHandler()
                    

class MyServer(SimpleHTTPRequestHandler):
    def do_POST(self):
        
        if self.path != '/radio.queue':
            print(self.path)
            self.send_error(404)
            self.end_headers()
            return
        
        try:
            rawData = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(rawData)
            if data['command'] == 'register':
                radio.registerClient(data['id'])
                response = 201
            elif data['command'] == 'add':
                radio.addToQueue(data['message'])
                response = 201
            elif data['command'] == 'read':
                result = radio.readFromQueue(data['id'])
                response = 200
            else:
                print('Invalid command ' + data['command'])
                self.send_error(400)
                self.end_headers()
                return
        except Exception as e:
            print('Invalid request ' + repr(e))
            self.send_error(400)
            self.end_headers()
            return
        
        self.send_response(response)
        self.send_header("Content-Type", "application/json")
        if response == 200:
            output = {"result": result}
            rawOutput = bytes(json.dumps(output), "utf-8")
            outLength = len(rawOutput)
            self.send_header("Content-Length", outLength)
            self.end_headers()
            self.wfile.write(rawOutput)
        else:
            self.send_header("Content-Length", 0)
            self.end_headers()


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")