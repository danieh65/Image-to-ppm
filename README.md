# Image to ppm
This program is intended to take an image file and convert it into a P3 .ppm file. This can be done in two ways:
## Python Script (```Image_to_ppm.py```)
To run the script, you will need numpy, OpenCV, and skimage packages installed. If you don't, you can install them with 

```
pip3 install numpy
pip3 install scikit-image
pip3 install opencv-python
```

Then, to run the script, all you need to do is run the command
```python3 Image_to_ppm.py <source_image>```. It will create a new .ppm file in the same directory where you run the script. Note you do not actually have to be in the same directory as ```Image_to_ppm.py```, but it saves you having to write out the full filepath.

## Executable
If you don't want to install a bunch of python packages, you can run it from the compiled executable. To do so, run the following command:

```<filepath to Image_to_ppm executable> <filepath to image>```

Example:
``` bash
Daniels-MacBook-Air:~ danieh65$ cd Desktop
Daniels-MacBook-Air:Desktop danieh65$ ls
Everything_else			Two-byte grape.png
Executable			trump-laughter-un.jpg
Pictures			trump-laughter-un.new.ppm
Daniels-MacBook-Air:Desktop danieh65$ /Users/danieh65/Desktop/Executable/Compiled\ files/Image_to_ppm /Users/danieh65/Desktop/trump-laughter-un.jpg 
Daniels-MacBook-Air:Desktop danieh65$ echo "The following also works."
The following also works.
Daniels-MacBook-Air:Desktop danieh65$ /Users/danieh65/Desktop/Executable/Compiled\ files/Image_to_ppm trump-laughter-un.jpg 
Daniels-MacBook-Air:Desktop danieh65$ 
```

