# Library Imports
import geopandas as gpd
import rasterio as rio
import os
import gdal
import numpy as np

# Path for holding temporary files
temp_path = os.path.dirname(os.path.abspath(__file__)) + "/_temp/"


def crop(image_file, shape_file, heightmap=False):
    """"Crops a raster image using the limits of the shape file passed as parameter.

    If necessary, converts the CRS of the shape_file to be same as the image's.
    Following with the process, uses GDAL Warp method to cut the raster.
    The result is a saved image on a temporary path.
    The image is then opened as a raster using rasterio lib and converted to a numpy array.
    The temporary folder is deleted and the 'no-value' information is removed.
    Finally, the array is returned.

    Parameters
    ----------
    image_file: string
        Path to raster image file.
    shape_file: string
        Path to shapefile to be used as limits.
    heightmap: bool
        If True, normalizes the resulting array between zero and one.

    Returns
    -------
    result: ndarray
        Numpy array containing the values per position on the map.
    """
    # Create the temporary folder
    os.makedirs(temp_path, exist_ok=True)
    # Sets the temporary output file path
    output_temp = temp_path+"result.tif"
    # Holds the shape file path 
    crop_bound = shape_file

    # Opens the shape file and raster image using the libs
    shape = gpd.read_file(shape_file)
    image = rio.open(image_file)

    # if the CRS from the shapefile is different from the on the image
    if not shape.crs == image.crs and image.crs is not None:
        # sets the reprojected shape file path
        reproj_shp_path = temp_path + "_temp_reproj.shp"
        # reprojects the shapefile inplace
        shape.to_crs(crs=image.crs['init'], inplace=True)
        # saves the reprojected shape to file
        shape.to_file(reproj_shp_path)
        # holds the new shape file path
        crop_bound = reproj_shp_path
    # Cuts the raster image using the proper shapefile
    gdal.Warp(output_temp, image_file, cutlineDSName=crop_bound)
    # After cutting, opens the image as a raster object
    with rio.open(output_temp) as src:
        # reads the raster as a numpy array
        cropped = src.read()
    # After opening, deletes the temp folder
    _clear_temp()
    # removes the insignificant values from the array
    result = _remove_values(cropped, cropped.min())
    # if the heightmap parameter is passed
    if heightmap:
        # returns the normalized array
        return generate_heightmap(result)
    # returns the array containing the results
    return result


def _remove_values(im, near_null):
    """ Switches all values from the im array that match near_full value to NaN.

    First, drops all lines and/or columns that are completely formed by near_null values.
    Then, iterates through all elements of the array, swapping those necessary.

    Parameters
    ----------
    im: ndarray
        Numpy array to have its values changed.
    near_null: float
        Value to be swapped.

    
    Returns
    -------
    img: ndarray
        Array containing only relevant numeric values.
    """
    # tries to drop lines that contains only the near_null values
    # this try except ensures the array dimension is the correct one
    try:
        img = im[~np.all(im == near_null, axis=1)]
    except:
        img = im[~np.all(im == near_null, axis=2)]

    img = img[:, ~np.all(img == near_null, axis=0)]
    # Swaps the near null values to NaN
    for i in range(len(img[0])):
        for j in range(len(img[:, 0])):
            if img[j, i] == near_null:
                img[j, i] = 0.0
    return img


def _clear_temp():
    """Deletes all files inside the temporary folder and then deletes the folder.
    Uses this module temp_path as path.
    """
    # deletes all files inside the temp folder
    for file in os.listdir(temp_path):
        os.remove(temp_path+file)
    # deletes the temp folder
    os.removedirs(temp_path)


def generate_heightmap(array):
    """ Normalizes the array between zero and one.
    
    Parameters
    ----------
    array: ndarray
        Numpy array to be normalized.

    Returns
    -------
    array: ndarray
        Normalized array with values between zero and one.
    """
    from math import ceil
    # gets the maximum value of the array and rounds it up
    ceiling = ceil(np.nanmax(array))
    # defines the lambda function to normalize array
    normalize = np.vectorize(lambda i: i/ceiling)
    # returns the normalized array
    return normalize(array)
