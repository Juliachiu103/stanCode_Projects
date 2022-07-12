"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def main():
    """
    Combine the figure image and the background image
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, the figure image
    :return img: combined image without the green screen
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            figure_p = figure_img.get_pixel(x, y)
            background_p = background_img.get_pixel(x, y)
            bigger = max(figure_p.red, figure_p.blue)
            if figure_p.green > bigger*2:
                # green screen
                figure_p.red = background_p.red
                figure_p.green = background_p.green
                figure_p.blue = background_p.blue
    return figure_img


if __name__ == '__main__':
    main()
