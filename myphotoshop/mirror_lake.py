"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def main():
    """
    Create a "mirror lake" vibe by reflecting the original image and put it below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


def reflect(filename):
    """
    :param filename:str, the file path of the original image (with respect to current directory)
    :return img: SimpleImage, the image with inverse image below the original one
    """
    img = SimpleImage('images/mt-rainier.jpg')
    blank_image = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            # original image
            img_p = img.get_pixel(x, y)

            # upper image
            upper_p = blank_image.get_pixel(x, y)

            # below image
            below_p = blank_image.get_pixel(x, blank_image.height-1-y)

            upper_p.red = below_p.red = img_p.red
            upper_p.green = below_p.green = img_p.green
            upper_p.blue = below_p.blue = img_p.blue
    return blank_image


if __name__ == '__main__':
    main()
