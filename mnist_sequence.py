from __future__ import print_function
import numpy as np
from load import MNIST
from random import choice


class MNIST_Sequence(object):

    def __init__(self, path='data', name_img='t10k-images.idx3-ubyte',
                 name_lbl='t10k-labels.idx1-ubyte'):
        self.dataset = MNIST(path, name_img, name_lbl)
        self.images, self.labels = self.dataset.load()
        self.label_map = [[] for i in range(10)]
        self.__generate_label_map()

    def __calculate_uniform_spacing(self, size_sequence, minimum_spacing, maximum_spacing,
                                    total_width, image_width=28):
        if size_sequence <= 1:
            return 0
        allowed_spacing = (total_width - size_sequence * image_width) / ((size_sequence - 1) * 1.0)
        if not allowed_spacing.is_integer() or allowed_spacing < minimum_spacing \
                or allowed_spacing > maximum_spacing:
            print("Uniform spacing is not possible for the given set of values, " +
                  "please provide suitable values.")
            print("For example, try with sequence [0, 1] with minimum spacing 0, " +
                  "maximum_spacing 10 and image_width 66.")
            exit()
        return allowed_spacing

    def __generate_label_map(self):
        num_labels = len(self.labels)
        for i in range(num_labels):
            self.label_map[self.labels[i]].append(i)

    def __select_random_label(self, label):
        if len(self.label_map[label]) > 0:
            return choice(self.label_map[label])
        else:
            print("No images for the number " + str(label) +
                  " is available. Please try with a different number.")
            exit()

    def generate_image_sequence(self, sequence, minimum_spacing, maximum_spacing,
                                total_width, image_height=28):
        sequence_length = len(sequence)
        allowed_spacing = self.__calculate_uniform_spacing(sequence_length, minimum_spacing,
                                                           maximum_spacing, total_width)
        spacing = np.ones(image_height * allowed_spacing,
                          dtype='float32').reshape(image_height, allowed_spacing)
        random_label_number = self.__select_random_label(sequence[0])
        image = self.images[random_label_number]
        for i in range(1, sequence_length):
            if i < sequence_length:
                image = np.hstack((image, spacing))
            random_label_number = self.__select_random_label(sequence[i])
            image = np.hstack((image, self.images[random_label_number]))
        return image
