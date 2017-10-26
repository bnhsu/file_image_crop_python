# written by bnhsu 2017
# croping all the images in the file into the same size 

from PIL import Image
import numpy as np
import glob

box = (0, 142, 291, 284)
path = '/home/username/folder/'
for filename in glob.glob("*.png"):
	im = Image.open(filename)
	print im.format, im.size, im.mode
	im_crop = im.crop(box)
	newName = "c_" + filename
	print newName 
	im_crop.save(path + newName)

