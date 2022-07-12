"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 0.8
WHITE = 650


def main():
    """
    創作理念 :
    Play as the Queen holding an apple in the Snow White story.
    """
    fig = SimpleImage("image_contest/Julia.jpg")  # 1030x628
    fig.show()
    bg = SimpleImage("image_contest/mirror.jpg")  # 795x339
    bg.make_as_big_as(fig)  # 1030x628
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            total = fig_pixel.red + fig_pixel.green + fig_pixel.blue
            if fig_pixel.red > 180*THRESHOLD and fig_pixel.green > 200*THRESHOLD and fig_pixel.blue > 165*THRESHOLD:
                # try to pick out the color of the background(米色)
                if total < WHITE:
                    # try to keep the white color on the mask
                    bg_pixel = bg.get_pixel(x, y)
                    fig_pixel.red = bg_pixel.red
                    fig_pixel.green = bg_pixel.green
                    fig_pixel.blue = bg_pixel.blue
    return fig

if __name__ == '__main__':
    main()
