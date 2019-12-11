from websocket.Messages.Message import Message

"""
This file holds classes of the custom messages to be sent to the receiving socket.
Each of the classes must extend from message.
Also, all message types must be defined on the top section of the file.
"""

HEIGHTMAP_TYPE = 'heightmap'
TEXT_TYPE = 'text'


class HeightmapMessage(Message):

    def __init__(self, values=None):
        super().__init__(message_type=HEIGHTMAP_TYPE, data_dict={'heightmap': values})


class TextMessage(Message):

    def __init__(self, text=None):
        super().__init__(message_type=TEXT_TYPE, data_dict={'text': text})
