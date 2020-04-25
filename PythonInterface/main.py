from interface import App, AppDelegate
from gis_manager import crop

import numpy as np
import pandas as pd

from websocket.server import start_server
from websocket.Messages.UserMessages import TextMessage, HeightmapMessage

"""
Implements the App Delegate protocol to set the file paths.
"""
class Delegate(AppDelegate):

    def __init__(self):
        self.image_path = ""
        self.shape_path = ""

    def get_shape_path(self, file_path):
        self.shape_path = file_path

    def get_image_path(self, file_path):
        self.image_path = file_path


if __name__ == "__main__":
    # Initializes the delegate object
    delegate = Delegate()
    # initializes the app
    application = App(delegate=delegate)
    # after the plot button is pressed, gets the file paths from the delegate object
    if delegate.shape_path != "" and delegate.shape_path != "":
        # crops the map image
        cropped_image = crop(image_file=delegate.image_path, shape_file=delegate.shape_path, heightmap=False)
    else:
        raise Exception("Files not selected.")
    
    print("Starting websocket server...")
    messages = []

    # Initialize message containing heightmap.
    hmap = HeightmapMessage(values=cropped_image)
    # Initialize text message to print after transmitting heightmap.
    txt_msg = TextMessage("Heightmap trasmitted successfuly.")
    # Append messages to list.
    messages.append(hmap)
    messages.append(txt_msg)
    # Starting server
    start_server(messages)
