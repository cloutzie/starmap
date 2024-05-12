import numpy as np
from PIL import Image
import random
import math

x = np.arange(0, 1920)
y = np.arange(0, 1080)
arr = np.zeros((y.size, x.size))


for _ in range(10):
    cx = random.randint(100, x.size-100)
    cy = random.randint(100, y.size-100)
    r = random.randint(3, 6)

    star = (x[np.newaxis,:]-cx)**2 + (y[:,np.newaxis]-cy)**2 < r**2
    arr[star] = 255

img = Image.fromarray(arr)
#img.save("your_file.jpeg")
img.show()