from websocket.Messages.UserMessages import TextMessage, HeightmapMessage
from websocket.server import start_server

from interface import App, AppDelegate
from gis_manager import crop

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


def array_to_file(array, output_path=None):
    """
    Converts the array to a dataframe and saves it to a file.
    """
    # Arrays used to setup Dataframe
    x_coordinates = []
    y_coordinates = []
    im_value = []

    # Generates dataframe
    if output_path is not None:
        # Separates the arrays
        for i in range(len(array[0])):
            for j in range(len(array[:, 0])):
                im_value.append(array[j, i])
                x_coordinates.append(j)
                y_coordinates.append(i)

        # Converts numpy array to dataframe.
        x_array = np.array(x_coordinates)
        y_array = np.array(y_coordinates)
        values_array = np.array(im_value)

        dataframe = pd.DataFrame({'x': x_array, 'y': y_array, 'value': values_array})
        dataframe.to_csv(path_or_buf=output_path, index=False, header=False, sep=';')


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

    array_to_file(cropped_image, output_path="/Users/rafaelprado/Code/ImmMaps/MapPlot/assets/input/map_input.csv")

    # messages = []
    # messages.append(TextMessage(text="Transmitting dataset..."))
    # messages.append(HeightmapMessage(values=cropped_image))
    # start_server(message_list=messages)

