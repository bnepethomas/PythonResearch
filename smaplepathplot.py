import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.image as image
import matplotlib.pyplot as plt

import numpy as np

image_path = "./images/"
image_name = 'FloorPlanCopy.png'
original_image_name = 'FloorPlanOriginal.png'

im = image.imread(image_path + original_image_name)
im[1, 1, 1] = 0 # set the alpha channel

fig, ax = plt.subplots()

ax.set_alpha(1)

Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.LINETO, (0.35, -1.1)),
    (Path.LINETO, (-1.75, 2.0)),
    (Path.LINETO, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.LINETO, (2.2, 3.2)),
    (Path.LINETO, (3, 0.05)),
    (Path.LINETO, (2.0, -0.5)),
    
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)



x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')



fig.figimage(im, 10, 10, zorder=-11)


ax.grid('off')
ax.axis('off')

plt.savefig(image_path + image_name, format='png', dpi=200)

plt.show()
