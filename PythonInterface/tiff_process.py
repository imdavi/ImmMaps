from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def tiff_to_dataframe(path):
    # Arrays used to setup Dataframe
    x_coordinates = []
    y_coordinates = []
    im_value = []

    # Creating the numpy array from image
    im = Image.open(path)
    im = np.array(im)
    # Obtains the minimal value of the entire array
    min_val = find_near_null(im)

    # Removes all near-null lines or columns from the image.
    im = remove_near_null(im, min_val)
    # Swaps the near null values to None
    for i in range(len(im[0])):
        for j in range(len(im[:,0])):
            # Coloca os valores em cada array 
            im_value.append(im[j,i])
            x_coordinates.append(j)
            y_coordinates.append(i)

    # Conversao de numpy array para dataframe
    x_array = np.array(x_coordinates)
    y_array = np.array(y_coordinates)
    values_array = np.array(im_value)

    dataframe = pd.DataFrame({'x':x_array, 'y':y_array, 'value':values_array})
    return dataframe

def find_near_null(image):
    min_value = float("inf")
    for i in range(len(image[0])):
        for j in range(len(image[:,0])):
            if image[j,i] < min_value:
                min_value = image[j,i]
    
    return min_value

def remove_near_null(im, near_null):
    img = im[~np.all(im == near_null, axis=1)]
    img = img[:,~np.all(img == near_null, axis=0)]
    # Swaps the near null values to None
    for i in range(len(img[0])):
        for j in range(len(img[:,0])):
            if img[j,i] == near_null:
                img[j,i]= None
    
    return img

if __name__ == "__main__":
    # Main apenas para debug
    image_path = "/Users/rafaelprado/Downloads/cps_df.tif"
    output_path = "/Users/rafaelprado/Code/ImmMaps/MapPlot/Assets/input/_input.csv"
    print("Starting image processing...")
    df = tiff_to_dataframe(image_path)
    print("Image converted to dataframe.\nNow dumping output file...")
    df.to_csv(path_or_buf=output_path, index=False, header=False, sep=';')
    print("Dumping complete!")