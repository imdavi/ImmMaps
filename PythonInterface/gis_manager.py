import geopandas as gpd
import rasterio as rio
import earthpy.spatial as es
import numpy as np


def crop(image_file, shape_file, return_meta=False):
    # Loads the SHP and the image file
    crop_frontier = gpd.read_file(shape_file)
    image = rio.open(image_file)

    # Checks if image has coordinate system
    if image.crs is None:
        raise Exception("Image file must have a coordinate system.")
    # Acquires the image coordinate system to apply to the dataframe
    image_crs = image.crs.data['init'].split(':')[1]

    # Apply image CRS to SHP
    crop_frontier = crop_frontier.to_crs(epsg=image_crs)
    # Crops the image, masking with the SHP
    data, meta = es.crop_image(image, crop_frontier)

    if return_meta:
        return data, meta
    else:
        return data[0]


def remove_values(im, near_null):
    img = im[~np.all(im == near_null, axis=1)]
    img = img[:, ~np.all(img == near_null, axis=0)]
    # Swaps the near null values to None
    for i in range(len(img[0])):
        for j in range(len(img[:, 0])):
            if img[j, i] == near_null:
                img[j, i] = np.nan
    return img


def generate_heightmap(array):
    from math import ceil

    ceiling = ceil(np.nanmax(array))

    normalize = np.vectorize(lambda i: i/ceiling)
    return normalize(array)



