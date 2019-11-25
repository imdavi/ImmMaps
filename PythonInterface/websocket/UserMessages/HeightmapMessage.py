from websocket.Messages.Message import Message

_MESSAGE_TYPE = 'heightmap'


class HeightmapMessage(Message):

    def __init__(self, values=None):
        super().__init__(message_type=_MESSAGE_TYPE, data_dict={'heightmap': values})
