from websocket.Messages.Message import Message

_MESSAGE_TYPE = 'error'


class ErrorMessage(Message):

    def __init__(self, cause=None):
        super().__init__(message_type=_MESSAGE_TYPE, data_dict={'cause': cause})
