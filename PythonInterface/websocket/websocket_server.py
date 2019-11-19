from tornado.websocket import WebSocketHandler

import tornado.ioloop
import tornado.web
import tornado.websocket
from PIL import Image
import io
import json
import base64
import numpy as np

_FIELD_TYPE = 'type'
_FIELD_CAUSE = 'cause'
_FIELD_IMAGE_PATH = 'image_path'
_FIELD_IMAGE = 'image'
_FIELD_IMAGE_MODE = 'image_mode'
_FIELD_IMAGE_FORMAT = 'image_format'
_FIELD_IMAGE_HEIGHT = 'image_height'
_FIELD_IMAGE_WIDTH = 'image_width'
_FIELD_HEIGHTMAP = 'heightmap'

_TYPE_ERROR = 'error'
_TYPE_GET_IMAGE = 'get_image'
_TYPE_LOAD_IMAGE = 'load_image'
_TYPE_IMAGE = 'image'
_TYPE_HEIGHTMAP = 'heightmap'
_TYPE_GET_HEIGHTMAP = 'get_heightmap'


class ImmVisWebSocket(tornado.websocket.WebSocketHandler):
    image_path = None
    original_image = None

    def initialize(self, image_path=None):
        self.load_image(image_path)

    def load_image(self, image_path=None):
        self.image_path = image_path

        try:
            self.original_image = Image.open(self.image_path)
        except:
            self.original_image = None
            return False

        return True

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print("On message started...")
        try:
            payload = json.loads(message)
        except:
            return self.send_error_message(u'Unexpected request format')

        message_type = payload.get(_FIELD_TYPE)

        if message_type == _TYPE_LOAD_IMAGE:
            image_path = payload.get(_FIELD_IMAGE_PATH)
            if self.load_image(image_path):
                self.send_original_image()
            else:
                self.send_error_message(u'Failed to load image.')

        elif message_type == _TYPE_GET_IMAGE:
            self.send_original_image()

        elif message_type == _TYPE_GET_HEIGHTMAP:
            self.send_original_image_heightmap()

        else:
            self.send_error_message(u'Unknown request type.')

    def send_original_image_heightmap(self):
        if self.original_image is not None:
            self.send_image_heightmap(self.original_image)
        else:
            self.send_error_message(u'Image is not available')
    
    def send_image_heightmap(self, image):

        heightmap = np.asarray(image)
        width, height = image.size

        response_message = self.create_response_message(
            {
                _FIELD_TYPE: _TYPE_HEIGHTMAP,
                _FIELD_IMAGE_FORMAT: image.format,
                _FIELD_IMAGE_WIDTH: width,
                _FIELD_IMAGE_HEIGHT: height,
                _FIELD_HEIGHTMAP: heightmap
            }
        )
        print("Sending heightmap...")
        self.write_message(response_message)

    def send_original_image(self):
        if self.original_image is not None:
            self.send_image(self.original_image)
        else:
            self.send_error_message(u'Image is not available')

    def send_image(self, image):
        buffer = io.BytesIO()
        image.save(buffer, format=image.format)
        image_string = base64.b64encode(buffer.getvalue()).decode('utf-8')
        width, height = image.size

        response_message = self.create_response_message(
            {
                _FIELD_TYPE: _TYPE_IMAGE,
                _FIELD_IMAGE_FORMAT: image.format,
                _FIELD_IMAGE_MODE: image.mode,
                _FIELD_IMAGE_WIDTH: width,
                _FIELD_IMAGE_HEIGHT: height,
                _FIELD_IMAGE: image_string
            }
        )

        self.write_message(response_message)

    def send_error_message(self, cause):
        message = self.create_response_message(
            {
                _FIELD_TYPE: _TYPE_ERROR,
                _FIELD_CAUSE: cause
            }
        )
        self.write_message(message)

    def create_response_message(self, data_dict):
        return json.dumps(data_dict, cls=NumpyEncoder)

    def on_close(self):
        print("WebSocket closed")


def create_app(message=None):
    try:
        return tornado.web.Application([
            (r"/websocket", ImmVisWebSocket, message)
        ])
    except Exception as error:
        raise Exception("MessageNotFound - "+str(error))


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def start_server(message=None, port=8888):
    socket = create_app(message)
    socket.listen(port)

    print("Starting server: http://localhost:" + str(port) + "/")

    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":

    img_path = "./_img/cps_df.tif"

    message = {
        'image_path': img_path
    }

    start_server(message)