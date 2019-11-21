from websocket.server import start_server
from websocket.UserMessages.TextMessage import TextMessage
from matplotlib import pyplot as plt

from gis_manager import crop, remove_values, generate_heightmap

if __name__ == "__main__":
    root_path = "/Users/rafaelprado/Code/ImmMaps/PythonInterface/"
    img_path = root_path + "_img/"
    shp_path = root_path + "_shapes/"

    cps_shp_name = "Campinas.shp"
    img_original = "cps_df.tif"

    cropped = crop(img_path+img_original, shp_path+cps_shp_name)

    cropped = remove_values(cropped, cropped.min())

    plt.imshow(cropped, cmap='hot')
    plt.colorbar()
    plt.show()

    new_crop = generate_heightmap(cropped)
    plt.imshow(new_crop, cmap='hot')
    plt.colorbar()
    plt.show()
    # messages = []
    # messages.append(TextMessage(text="Generic message test successful."))
    # messages.append(TextMessage(text="It fucking works!."))
    # start_server(message_list=messages)
