from __future__ import print_function
from mnist_sequence_api import MNIST_Sequence_API
import sys


def main():
    arguments = list(sys.argv[1:])
    if len(arguments) == 4:
        sequence, min_spacing = list(map(int, list(arguments[0])), int(arguments[1]))
        max_spacing, image_width = int(arguments[2]), int(arguments[3])
        api_object = MNIST_Sequence_API()
        img_data = api_object.generate_mnist_sequence(sequence, (min_spacing, max_spacing), image_width)
        api_object.save_image(img_data, sequence)
    else:
        print("Incorrect number of arguments.")
        print("Usage: python mnist_sequence_cli.py <sequence(no spaces) " +
              "min_spacing max_spacing image_width>")

if __name__ == "__main__":
    main()
