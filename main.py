"""
The  final result of the script is to output the whole product as a sigma0 form
http://step.esa.int/docs/tutorials/Performing%20SAR%20processing%20in%20Python%20using%20snappy.pdf
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os
import snappy
from snappy import Product
from snappy import ProductIO
from snappy import ProductUtils
from snappy import WKTReader
from snappy import HashMap
from snappy import GPF
import os.path
from os import path

### Reading the product subset
subset_path = 'dataset/subset_0_of_S1A_IW_GRDH_1SDV_20191004T011831_20191004T011856_029302_035471_E23D.dim'
if path.exists(subset_path):
    try:
        product = ProductIO.readProduct("dataset/subset_0_of_S1A_IW_GRDH_1SDV_20191004T011831_20191004T011856_029302_035471_E23D.dim")
    except:
        print("error reading file")
else:
    print("file not found")

print("Reading...")
width = product.getSceneRasterWidth()
print("Width: {} px".format(width))
height = product.getSceneRasterHeight()
print("Height: {} px".format(height))
name = product.getName()
print("Name: {}".format(name))
band_names = product.getBandNames()
print("Band names: {}".format(", ".join(band_names)))

### 