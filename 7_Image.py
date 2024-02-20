import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# matplotlib can be used to display image---------------------

# download image
from urllib.request import urlretrieve
urlretrieve('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Red_Kitten_01.jpg/640px-Red_Kitten_01.jpg', 'cat.jpg')

# before image displayed, it has to be read into memory using Python Imaging Library (PIL) module
from PIL import Image
img = Image.open('cat.jpg')   # open image into memory
print(type(img))

# display the image
plt.title('A cat staring')
plt.grid(False)     # grid lines don't come
# plt.axis('off')
plt.imshow(img)

# image array
img_arr = np.array(img)
print(img_arr.shape)
plt.imshow(img_arr[50:350, 240:500])    # shows image in the range

# to show image
plt.show()
