from __future__ import print_function
import os
import struct
from array import array
import numpy as np


class MNIST(object):

    def __init__(self, path='data', name_img='t10k-images.idx3-ubyte',
                 name_lbl='t10k-labels.idx1-ubyte'):
        self.path = path
        self.name_img = name_img
        self.name_lbl = name_lbl

    def load(self):
        path_img = os.path.join(os.getcwd(), self.path, self.name_img)
        path_lbl = os.path.join(os.getcwd(), self.path, self.name_lbl)

        with open(path_lbl, 'rb') as f:
            magic, size = struct.unpack(">II", f.read(8))

            if magic != 2049:
                print('Magic number mismatch, expected 2049,''got {}'.format(magic))
                exit()

            labels = array("B", f.read())

        with open(path_img, 'rb') as f:
            magic, size, rows, cols = struct.unpack(">IIII", f.read(16))

            if magic != 2051:
                print('Magic number mismatch, expected 2051,''got {}'.format(magic))
                exit()

            image_data = list(map(lambda pixel: (255 - pixel) / 255.0, array("B", f.read())))
            # Converting data to 32 bit floating point range from 0 (black) to 1 (white)

            images = np.asarray(image_data, dtype=np.float32).reshape(size, rows, cols)

        return images, labels
