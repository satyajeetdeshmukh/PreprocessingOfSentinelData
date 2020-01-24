from snappy import jpy, Band, ProductIO, ProductUtils, ProgressMonitor
import os.path
from os import path

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
height = product.getSceneRasterHeight()
name = product.getName()
desc = product.getDescription()
band_names = product.band_names()

print("Product: %s, %d x %d pixels, %s" % (name, width, height, desc))
print("Bands:   %s" % (band_names))

