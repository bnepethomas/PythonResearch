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
np.random.seed(19680801)

image_path = "./images/"
image_name = 'FloorPlanCopy.png'

datafile = cbook.get_sample_data('logo2.png', asfileobj=False)
print('loading %s' % datafile)
im = image.imread(image_path + image_name)
im[1, 1, 1] = 0 # set the alpha channel

fig, ax = plt.subplots()
plt.scatter(0.5,0.5, facecolor='r', edgecolor='r')
ax.plot(np.random.rand(20), '-o', ms=20, lw=2, alpha=1, mfc='green')
ax.grid()
# negative z order puts image behind the graph
fig.figimage(im, 10, 10, zorder=-11)

plt.axis('off')
plt.savefig(buff, format='png', dpi=500)
plt.show()
