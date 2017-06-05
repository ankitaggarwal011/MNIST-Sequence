# MNIST Digit Sequence Generator: Images representing sequence of digits using the MNIST handwritten digit image dataset

## Problem

The MNIST database is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. The goal of this project is to use the above database of handwritten digit images to generate images representing sequences of handwritten digits.

These images could be used to train classifiers and generative deep learning models.

## Solution

A script that saves examples of generated images is helpful in inspecting the characteristics of the generated images and in inspecting the trained models behaviors.

## Dependencies

## Setup

## Examples

## API:

```
generate_mnist_sequence(digits, spacing_range, image_width)
```

where:
 
- `digits` is a list-like containing the numerical values of the digits from which the sequence will be generated (for example `[3, 5, 0]`) 
- `spacing_range` is a tuple containing the minimum and maximum spacing (in pixels) between digits. 
- `image_width` specifies the width of the image in pixels.

The function returns a (28 x image_width) image.

Images are represented as floating point 32 bits numpy arrays with a scale ranging from 0 (black) to 1 (white), the first dimension corresponding to the height and the second dimension to the width.

## Script

The CLI script takes positional arguments: 

- <sequence>: the sequence of digits to be generated 
- <min_spacing>: minimum spacing between consecutive digits
- <max_spacing>: maximum spacing between consecutive digits
- <image_width>: width of the generated image

The generated image is saved in the current directory as a <sequence>.png, for example, 1-2-3.png.

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