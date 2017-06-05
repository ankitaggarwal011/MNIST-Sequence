from __future__ import print_function
from load import MNIST
from mnist_sequence import MNIST_Sequence
from mnist_sequence_api import MNIST_Sequence_API
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
        return (rows == 28 and cols == 66)

    def mnist_sequence_api_test(self):
        self.mnist_sequence_api.generate_mnist_sequence([0, 1], (0, 10), 66)
        return os.path.isfile("0-1.png")


def run_tests():
    tests = Tests()
    total_tests, test_count = 3, 0
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
    print(str(test_count) + " / " + str(total_tests) + " were passed.")

if __name__ == "__main__":
    run_tests()
