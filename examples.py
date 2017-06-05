from __future__ import print_function
from mnist_sequence_api import MNIST_Sequence_API


api_object = MNIST_Sequence_API()

api_object.save_image(api_object.generate_mnist_sequence(range(8), (0, 10), 224), range(8))
api_object.save_image(api_object.generate_mnist_sequence(range(9), (0, 10), 292), range(9))
api_object.save_image(api_object.generate_mnist_sequence(range(10), (0, 10), 280), range(10))
