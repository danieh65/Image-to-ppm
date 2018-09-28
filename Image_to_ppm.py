import os,glob,cv2
import sys,argparse
import numpy as np
from skimage import img_as_ubyte as ubyte

dir_path = os.path.dirname(os.path.realpath(__file__))
image_path=sys.argv[1]
filename = image_path
if dir_path not in image_path:
    filename = dir_path +'/' +image_path
tokens = image_path.split('.')
tokens.pop()
tokens.append("new")
tokens.append("ppm")
new_filename = '.'.join(tokens)

image = cv2.imread(filename)

if image is None:
    print(filename + " could not be loaded")
    exit()

image = ubyte(image)

form = "P3"
max_value = 255
height, width, channels = image.shape

f = open(new_filename, "w")

f.write(form + '\n')
f.write (str(width) + " " + str(height) + '\n')
f.write(str(max_value) + '\n')

for r in range(height):
    for c in range(width):
        for ch in reversed(range(channels)):
            f.write(str(image[r, c, ch]) + " ")
    f.write('\n')
