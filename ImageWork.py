import cgi, requests, json, base64, PIL, re, uuid, os, sys

from PIL import Image


import matplotlib.pyplot as plt

import matplotlib.image as mpimg
import numpy as np

requests.packages.urllib3.disable_warnings()
from requests.auth import HTTPBasicAuth

from io import BytesIO
import grequests as async

# Used for the storeMemory function.
buff = BytesIO()



def storeMemory(item):

    # Use cStringIO to write the item to memory.
    buff.write(item)

    # Go back to the start of the item.
    buff.seek(0)

    # Return the item we just stored.
    return buff.getvalue()


def create_test_image():
    file = BytesIO()
    image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file

# This is the path for the floorplan image files should be stored.
image_path = "./images/"
image_name = 'FloorPlanCopy.png'

if os.path.isfile(image_path + image_name  ) == True:
    print("File is here")  
    file = image_path + image_name 
    fh = open(file, "rb")
    print("Stand by")
    # image = storeMemory(fh.read()).b64encode("base64").strip()
    print("Exited")
    fh.close()
else:
    print("File is not here")

#create_test_image()

img = mpimg.imread(image_path + image_name)
print(img)
imgplot = plt.imshow(img)
print("Image shown")

    
                
