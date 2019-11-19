from tornado.websocket import WebSocketHandler

import tornado.ioloop
import tornado.web
import tornado.websocket
import json

from websocket.Messages.ErrorMessage import ErrorMessage

_FIELD_TYPE = 'type'
_RECEIVER_READY = 'client_ready'


def start_server(message_list=None, port=8888):
    # Creates a websocket server instance
    socket = tornado.web.Application([
            (r"/websocket", _ImmVisWebSocket, {'message_list': message_list})
        ])

    if message_list is None:
        print("WARNING - No message given on server initialization")

    socket.listen(port)
    print("Starting server: http://localhost:" + str(port) + "/")
    # initializes the infinite IO loop for the server
    tornado.ioloop.IOLoop.current().start()


class _ImmVisWebSocket(tornado.websocket.WebSocketHandler):
    message_list = None

    def initialize(self, message_list=None):
        if message_list is not None:
            self.message_list = message_list
        else:
            self.message_list = []

    def open(self):
        print("WebSocket opened.")

    def on_close(self):
        print("WebSocket closed.")

    def on_message(self, received_message):
        print("LOG - Message received")
        try:
            payload = json.loads(received_message)
            received_message_type = payload.get(_FIELD_TYPE)
            print("LOG - Message type: "+received_message_type)
        except:
            return self.send_error_message(u'Unexpected request format')

        if received_message_type == _RECEIVER_READY:
            for message in self.message_list:
                print("Sending message...")
                self.write_message(message.to_json())

    def send_error_message(self, cause):
        message = ErrorMessage(cause=cause)
        self.write_message(message.to_json())
