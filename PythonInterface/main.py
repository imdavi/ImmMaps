from websocket.Messages.UserMessages import TextMessage, HeightmapMessage
from websocket.server import start_server

from interface import App, AppDelegate
from gis_manager import crop
from tiff_process import tiff_to_dataframe


class Delegate(AppDelegate):

    def __init__(self):
        self.image_path = ""
        self.shape_path = ""

    def get_shape_path(self, file_path):
        self.shape_path = file_path

    def get_image_path(self, file_path):
        self.image_path = file_path


if __name__ == "__main__":
    delegate = Delegate()
    application = App(delegate=delegate)

    if delegate.shape_path != "" and delegate.shape_path != "":
        cropped_image = crop(image_file=delegate.image_path, shape_file=delegate.shape_path, heightmap=False)
    else:
        raise Exception("Files not selected.")

    tiff_to_dataframe(cropped_image, output_path="/Users/rafaelprado/Code/ImmMaps/MapPlot/assets/input/map_input.csv")

    # messages = []
    # messages.append(TextMessage(text="Transmitting dataset..."))
    # messages.append(HeightmapMessage(values=cropped_image))
    # start_server(message_list=messages)

