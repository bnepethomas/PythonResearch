"""
===============
Watermark image
===============

Use a PNG file as a watermark
"""
from __future__ import print_function
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.pyplot as plt

from io import BytesIO

buff = BytesIO()

# Fixing random state for reproducibility
np.random.seed()

image_path = "./images/"
image_name = 'FloorPlanCopy.png'
original_image_name = 'FloorPlanOriginal.png'

im = image.imread(image_path + original_image_name)
img2=np.ndarray(im.shape)

im[1, 1, 1] = 0 # set the alpha channel

fig, ax = plt.subplots()
plt.scatter(0.5,0.5, facecolor='r', edgecolor='r')
ax.plot(np.random.rand(20), '-o', ms=2, lw=2, alpha=1, mfc='green')
ax.grid()
# negative z order puts image behind the graph
fig.figimage(im, 10, 10, zorder=-11)

plt.axis('off')
plt.savefig(image_path + image_name, format='png', dpi=200)



#plt.imsave(image_path + image_name, img2, vmin=None, vmax=None, cmap=None, format=None, origin=None, dpi=100)
#    imsave(fname, arr, vmin=None, vmax=None, cmap=None, format=None, origin=None, dpi=100)
plt.show()
