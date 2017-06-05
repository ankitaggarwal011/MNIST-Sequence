from __future__ import print_function
from load import MNIST
from mnist_sequence import MNIST_Sequence
from mnist_sequence_api import MNIST_Sequence_API
import numpy as np
import os


class Tests(object):

    def __init__(self):
        self.mnist = MNIST()
        self.mnist_sequence = MNIST_Sequence()
        self.mnist_sequence_api = MNIST_Sequence_API()

    def load_test(self):
        images, labels = self.mnist.load()
        size, rows, cols = images.shape
        return (rows == cols == 28 and size == len(labels))

    def generate_image_sequence_test(self):
        img = self.mnist_sequence.generate_image_sequence([0, 1], 0, 10, 66)
        rows, cols = img.shape
        return (rows == 28 and cols == 66 and np.amax(img) == 1.0 and np.amin(img) == 0.0)

    def mnist_sequence_api_test(self):
        img = self.mnist_sequence_api.generate_mnist_sequence([0, 1], (0, 10), 66)
        rows, cols = img.shape
        return (rows == 28 and cols == 66 and np.amax(img) == 255 and np.amin(img) == 0)
    
    def save_image_test(self):
        self.mnist_sequence_api.save_image(self.mnist_sequence_api.generate_mnist_sequence([0, 1], (0, 10), 66), [0, 1])
        return os.path.isfile("0-1.png")


def run_tests():
    tests = Tests()
    total_tests, test_count = 4, 0
    if tests.load_test():
        test_count += 1
    else:
        print("Load test failed.")
    if tests.generate_image_sequence_test():
        test_count += 1
    else:
        print("Generate MNIST sequence test failed.")
    if tests.mnist_sequence_api_test():
        test_count += 1
    else:
        print("MNIST sequence API test failed.")
    if tests.save_image_test():
        test_count += 1
    else:
        print("Save image test failed.")
    print(str(test_count) + " / " + str(total_tests) + " were passed.")

if __name__ == "__main__":
    run_tests()
