from websocket.Messages.Message import Message

_MESSAGE_TYPE = 'text'


class TextMessage(Message):

    def __init__(self, text=None):
        super().__init__(message_type=_MESSAGE_TYPE, data_dict={'text': text})
