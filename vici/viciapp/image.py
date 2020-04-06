"""A set of utility functions for image processing"""

import os
from PIL import Image

def compress_under_size(size, file_path):
    '''file_path is a string to the file to be custom compressed
    and the size is the maximum size in bytes it can be which this 
    function searches until it achieves an approximate supremum'''

    quality = 20 #not the best value as this usually increases size

    current_size = os.stat(file_path).st_size

    if current_size <= size:
        return # Nothing to do
    
    while current_size > size or quality == 0:
        if quality == 0:
            os.remove(file_path.replace(".jpg","_c.jpg"))
            compress_pic(file_path, 1)
            print("Error: File cannot be compressed below this size")
            break

        compress_pic(file_path, quality)
        current_size = os.stat(file_path.replace(".jpg","_c.jpg")).st_size
        quality -= 5 
        print(quality)
    os.rename(file_path.replace('.jpg', '_c.jpg'), file_path)


def compress_pic(file_path, qual):
    '''File path is a string to the file to be compressed and
    quality is the quality to be compressed down to'''
    picture = Image.open(file_path)
    dim = picture.size

    picture.save(file_path.replace(".jpg","_c.jpg"),"JPEG", optimize=True, quality=qual)
