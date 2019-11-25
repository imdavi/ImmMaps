from gis_manager import crop

from websocket.Messages.UserMessages import TextMessage, HeightmapMessage
from websocket.server import start_server

if __name__ == "__main__":
    # root_path = "/Users/rafaelprado/Code/ImmMaps/PythonInterface/"
    # img_path = root_path + "_img/"
    # shp_path = root_path + "_shapes/"
    #
    # cps_shp_name = "Campinas.shp"
    # img_original = "tempsurperf_30ago2018.tif"
    #
    # cropped_image = crop(image_file=img_path+img_original, shape_file=shp_path+cps_shp_name, heightmap=True)

    messages = []
    messages.append(TextMessage(text="Transmitting dataset..."))
    # messages.append(HeightmapMessage(values=cropped_image))
    start_server(message_list=messages)

