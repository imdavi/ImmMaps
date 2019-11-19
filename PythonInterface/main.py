from tiff_process import tiff_to_dataframe
from websocket.server import start_server
import sys

from websocket.Messages.TextMessage import TextMessage

if __name__ == "__main__":
    messages = []
    messages.append(TextMessage(text="Generic message test successful."))
    messages.append(TextMessage(text="It fucking works!."))
    start_server(message_list=messages)
