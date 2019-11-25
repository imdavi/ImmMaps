import geopandas as gpd
import rasterio as rio
import numpy as np
import os
import gdal

temp_path = os.path.dirname(os.path.abspath(__file__)) + "/_temp/"


def crop(image_file, shape_file, heightmap=False):
    os.makedirs(temp_path, exist_ok=True)
    output_temp = temp_path+"result.tif"

    crop_bound = shape_file

    shape = gpd.read_file(shape_file)
    image = rio.open(image_file)

    if not shape.crs == image.crs and image.crs is not None:
        reproj_shp_path = temp_path + "_temp_reproj.shp"

        shape.to_crs(crs=image.crs['init'], inplace=True)
        shape.to_file(reproj_shp_path)
        crop_bound = reproj_shp_path

    gdal.Warp(output_temp, image_file, cutlineDSName=crop_bound)

    with rio.open(output_temp) as src:
        cropped = src.read()

    _clear_temp()

    result = _remove_values(cropped, cropped.min())

    if heightmap:
        return generate_heightmap(result)

    return result


def _remove_values(im, near_null):
    try:
        img = im[~np.all(im == near_null, axis=1)]
    except:
        img = im[~np.all(im == near_null, axis=2)]

    img = img[:, ~np.all(img == near_null, axis=0)]
    # Swaps the near null values to NaN
    for i in range(len(img[0])):
        for j in range(len(img[:, 0])):
            if img[j, i] == near_null:
                img[j, i] = np.nan
    return img


def _clear_temp():
    for file in os.listdir(temp_path):
        os.remove(temp_path+file)
    os.removedirs(temp_path)


def generate_heightmap(array):
    from math import ceil

    ceiling = ceil(np.nanmax(array))

    normalize = np.vectorize(lambda i: i/ceiling)
    return normalize(array)
