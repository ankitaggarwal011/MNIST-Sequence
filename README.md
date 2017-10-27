# MNIST Digit Sequence Generator: Images representing sequence of digits using the MNIST handwritten digit image dataset

## Problem

The [MNIST database](http://yann.lecun.com/exdb/mnist/) is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. The goal of this project is to use the above database of handwritten digit images to generate images representing sequences of handwritten digits.

These images could be used to train classifiers and generative deep learning models.

## Solution

The solution can be explained using the following steps:

- Decode the image and label MNIST data given in the special idx format with ```load.py```.
- Create a label hash map in which each key corresponds to a digit, and the values are the index of digits in the dataset. This will help us randomly choose handwritten image of any particular digit.
- Calculate allowed spacing according to the given values of minimum spacing, maximum spacing and image width using the formula: 
```allowed_spacing = (total_width - size_sequence * image_width) / ((size_sequence - 1) * 1.0)```. If the allowed spacing allows a uniform spacing for the sequence, move towards the generation of the image.
- Randomly choose an image index for each digit in the sequence. Next, horizontally stack each of these sequence digit images separated by uniformly spaced white background as per the allowed spacing. This is done in ```mnist_sequence.py```.
- Unit tests are available in ```tests.py```.
- An API endpoint is provided in ```mnist_sequence_api.py```.
- A CLI script is provided in ```mnist_sequence_cli.py```.A CLI script saves examples of generated images for inspecting the characteristics of the generated images and in inspecting the trained models behaviors.

The above algorithm is implemented in an object-oriented approach which allows great flexibility for future changes. In the API endpoint, the data is loaded only once which will help in scaling the solution. In the future, using parallel processing would improve program's response time.

## Dependencies

The library is supported for Python >= 2.7 and Python >= 3.3.

The python modules needed in order to use this library.
```
Pillow: 3.3.1
Numpy: 1.13.3 + mkl
```
Note: Numpy can be installed on a Windows machines using binaries provided over [here](http://www.lfd.uci.edu/%7Egohlke/pythonlibs).

## Tests

The tests can be run using the below command, currently there are 4 tests.

```
python tests.py
```

## Examples

The library currently uses the MNIST 10k test data samples, also available in the data folder with the project.

```
python examples.py
```

This will run generate three images of sequences and save them in the current directory.

```
python mnist_sequence_cli 01 0 10 66
```

This will run the CLI script, generate and save the image of the sequence ([0, 1]) of the digits with minimum spacing 0, maximum spacing 10 and width 66.

## API:

```
from mnist_sequence_api import MNIST_Sequence_API

api_object = MNIST_Sequence_API()
api_object.generate_mnist_sequence(digits, spacing_range, image_width)
```

where:
 
- `digits` is a list-like containing the numerical values of the digits from which the sequence will be generated (for example `[3, 5, 0]`) 
- `spacing_range` is a tuple containing the minimum and maximum spacing (in pixels) between digits. 
- `image_width` specifies the width of the image in pixels.

The function returns a (28 x image_width) image.

Images are represented as floating point 32 bits numpy arrays with a scale ranging from 0 (black) to 1 (white), the first dimension corresponding to the height and the second dimension to the width.

## Script

The CLI script takes positional arguments: 

- < sequence >: the sequence of digits to be generated 
- <min_spacing>: minimum spacing between consecutive digits
- <max_spacing>: maximum spacing between consecutive digits
- <image_width>: width of the generated image

The generated image is saved in the current directory as a < sequence >.png, for example, 1-2-3.png.

## License

[MIT License](https://github.com/ankitaggarwal011/MNIST-Sequence/blob/master/LICENSE)

## Contribute

Want to work on the project? Any kind of contribution is welcome!

Follow these steps:
- Fork the project.
- Create a new branch.
- Make your changes and write tests when practical.
- Commit your changes to the new branch.
- Send a pull request.