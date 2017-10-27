from __future__ import print_function
from mnist_sequence import MNIST_Sequence
import numpy as np
from PIL import Image


class MNIST_Sequence_API(object):

    def __init__(self):
        self.sequence_object = MNIST_Sequence(
            'data', 't10k-images.idx3-ubyte', 't10k-labels.idx1-ubyte')

    def generate_mnist_sequence(self, digits, spacing_range, image_width):
        img_data = (self.sequence_object.generate_image_sequence(digits, spacing_range[
                    0], spacing_range[1], image_width) * 255.0).astype(np.uint8)
        return img_data

    def generate_data(num_samples, seq_len, spacing_range=(0,0)):
        inputs = []
        labels = []
        for i in range(num_samples):
            seq_values = np.random.randint(0, 10, seq_len)
            seq = api_object.generate_mnist_sequence(seq_values, spacing_range, 28 * image_width)
            inputs.append(seq)
            labels.append(seq_values)
        return np.array(inputs), np.array(labels)

    def save_image(self, img_data, sequence):
        sequence_image = Image.fromarray(img_data)
        img_name = "-".join(list(map(str, sequence)))
        sequence_image.save(img_name + ".png")
        print("Image for the sequence " + img_name +
              " is generated and saved as " + img_name + ".png.")
