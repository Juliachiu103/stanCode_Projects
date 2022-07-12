"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def main():
    """
    Detect if there is a forest fire in the picture and highlight the area
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image (with respect to current directory)
    :return img: SimpleImage, the image with fire area highlight
    """
    img = SimpleImage('images/greenland-fire.png')
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = pixel.green = pixel.blue = avg
    return img


if __name__ == '__main__':
    main()
