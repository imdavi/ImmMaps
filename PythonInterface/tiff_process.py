from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def tiff_to_dataframe(input_path, output_path=None, image_output=None):
    # Arrays used to setup Dataframe
    x_coordinates = []
    y_coordinates = []
    im_value = []

    # Creating the numpy array from image
    im = Image.open(input_path)
    im = np.array(im)

    # Plot image using a "hot" color scale before processing
    # plot = plt.imshow(im, cmap='hot')
    # plt.colorbar()
    # plt.show()

    # Obtains the minimal value of the entire array
    min_val = find_near_null(im)

    # Removes all near-null lines or columns from the image.
    im = remove_near_null(im, min_val)

    # Plot image using a "hot" color scale
    # plot = plt.imshow(im, cmap='hot')
    # plt.colorbar()
    # plt.show()

    # Saves image to specified path
    if image_output is not None:
        Image.fromarray(im).save(image_output)

    # Generates dataframe
    elif output_path is not None:
        # Separates the arrays
        for i in range(len(im[0])):
            for j in range(len(im[:, 0])):
                im_value.append(im[j, i])
                x_coordinates.append(j)
                y_coordinates.append(i)

        # Converts numpy array to dataframe.
        x_array = np.array(x_coordinates)
        y_array = np.array(y_coordinates)
        values_array = np.array(im_value)

        dataframe = pd.DataFrame({'x': x_array, 'y': y_array, 'value': values_array})
        dataframe.to_csv(path_or_buf=output_path, index=False, header=False, sep=';')

        return dataframe


def find_near_null(image):
    min_value = float("inf")
    for i in range(len(image[0])):
        for j in range(len(image[:, 0])):
            if image[j, i] < min_value:
                min_value = image[j, i]
    
    return min_value


def remove_near_null(im, near_null):
    img = im[~np.all(im == near_null, axis=1)]
    img = img[:, ~np.all(img == near_null, axis=0)]
    # Swaps the near null values to None
    for i in range(len(img[0])):
        for j in range(len(img[:, 0])):
            if img[j, i] == near_null:
                img[j, i] = 0.0
    
    return img


if __name__ == "__main__":
    # Main apenas para debug
    img_path = "/Users/rafaelprado/Downloads/cps_df.tif"
    out_path = "/Users/rafaelprado/Desktop/immmaps.app/Contents/_input.csv"
    img_output = "/Users/rafaelprado/Desktop/mask_cps2.tif"
    tiff_to_dataframe(img_path, out_path, img_output)
