from websocket.Messages.Message import Message

HEIGHTMAP_TYPE = 'heightmap'
TEXT_TYPE = 'text'


class HeightmapMessage(Message):

    def __init__(self, values=None):
        super().__init__(message_type=HEIGHTMAP_TYPE, data_dict={'heightmap': values})


class TextMessage(Message):

    def __init__(self, text=None):
        super().__init__(message_type=TEXT_TYPE, data_dict={'text': text})
