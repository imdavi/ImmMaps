import json

_FIELD_TYPE = 'type'


class Message:
    message_type = None
    data_dict = None

    def __init__(self, message_type=None, data_dict=None):
        # Sets self type property
        self.message_type = message_type
        # Creates the first key of the dictionary for type
        dict_type = {_FIELD_TYPE: message_type}
        # Attributes to self dictionary
        self.data_dict = dict_type
        # Adds all other fields
        self.data_dict.update(data_dict)

    def to_json(self):
        return json.dumps(self.data_dict, cls=_NumpyEncoder)


class _NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        import numpy as np
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
