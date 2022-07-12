"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    Repeatedly blur the original image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img: SimpleImage, original image (smiley-face.png)
    :return: blurred image (smiley-face-blurred.png)
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            old_p = img.get_pixel(x, y)
            avg_r, avg_g, avg_b = avg_p(x, y, img, old_p)

            new_p = new_img.get_pixel(x, y)
            new_p.red = avg_r
            new_p.green = avg_g
            new_p.blue = avg_b
    return new_img


def avg_p(x, y, img, old_p):
    """
    Average the RGB values of original image's pixel's nearest neighbors
    """
    # surrounding points
    # p1 = img.get_pixel(x-1, y)
    # p2 = img.get_pixel(x+1, y)
    # p3 = img.get_pixel(x-1, y-1)
    # p4 = img.get_pixel(x, y-1)
    # p5 = img.get_pixel(x+1, y-1)
    # p6 = img.get_pixel(x-1, y+1)
    # p7 = img.get_pixel(x, y+1)
    # p8 = img.get_pixel(x+1, y+1)

    if x == 0 and y == 0:
        p2 = img.get_pixel(x+1, y)
        p7 = img.get_pixel(x, y+1)
        p8 = img.get_pixel(x+1, y+1)
        avg_r = (old_p.red + p2.red + p8.red + p7.red) // 4
        avg_g = (old_p.green + p2.green + p8.green + p7.green) // 4
        avg_b = (old_p.blue + p2.blue + p8.blue + p7.blue) // 4
    elif x == 0 and y == (img.height-1):
        p2 = img.get_pixel(x+1, y)
        p4 = img.get_pixel(x, y-1)
        p5 = img.get_pixel(x+1, y-1)
        avg_r = (old_p.red + p4.red + p2.red + p5.red) // 4
        avg_g = (old_p.green + p4.green + p2.green + p5.green) // 4
        avg_b = (old_p.blue + p4.blue + p2.blue + p5.blue) // 4
    elif x == (img.width-1) and y == 0:
        p1 = img.get_pixel(x-1, y)
        p6 = img.get_pixel(x-1, y+1)
        p7 = img.get_pixel(x, y+1)
        avg_r = (old_p.red + p1.red + p7.red + p6.red) // 4
        avg_g = (old_p.green + p1.green + p7.green + p6.green) // 4
        avg_b = (old_p.blue + p1.blue + p7.blue + p6.blue) // 4
    elif x == (img.width-1) and y == (img.height-1):
        p1 = img.get_pixel(x-1, y)
        p3 = img.get_pixel(x-1, y-1)
        p4 = img.get_pixel(x, y-1)
        avg_r = (old_p.red + p4.red + p1.red + p3.red) // 4
        avg_g = (old_p.green + p4.green + p1.green + p3.green) // 4
        avg_b = (old_p.blue + p4.blue + p1.blue + p3.blue) // 4
    elif x == 0 and (y != 0 or y != (img.height-1)):
        p2 = img.get_pixel(x + 1, y)
        p4 = img.get_pixel(x, y - 1)
        p5 = img.get_pixel(x + 1, y - 1)
        p7 = img.get_pixel(x, y + 1)
        p8 = img.get_pixel(x + 1, y + 1)
        avg_r = (old_p.red + p4.red + p5.red + p2.red + p8.red + p7.red) // 6
        avg_g = (old_p.green + p4.green + p5.green + p2.green + p8.green + p7.green) // 6
        avg_b = (old_p.blue + p4.blue + p5.blue + p2.blue + p8.blue + p7.blue) // 6
    elif x == (img.width-1) and (y != 0 or y != (img.height-1)):
        p1 = img.get_pixel(x - 1, y)
        p3 = img.get_pixel(x - 1, y - 1)
        p4 = img.get_pixel(x, y - 1)
        p6 = img.get_pixel(x - 1, y + 1)
        p7 = img.get_pixel(x, y + 1)
        avg_r = (old_p.red + p4.red + p7.red + p3.red + p1.red + p6.red) // 6
        avg_g = (old_p.green + p4.green + p7.green + p3.green + p1.green + p6.green) // 6
        avg_b = (old_p.blue + p4.blue + p7.blue + p3.blue + p1.blue + p6.blue) // 6
    elif y == 0 and (x != 0 or x != (img.width-1)):
        p1 = img.get_pixel(x - 1, y)
        p2 = img.get_pixel(x + 1, y)
        p6 = img.get_pixel(x - 1, y + 1)
        p7 = img.get_pixel(x, y + 1)
        p8 = img.get_pixel(x + 1, y + 1)
        avg_r = (old_p.red + p1.red + p2.red + p6.red + p7.red + p8.red) // 6
        avg_g = (old_p.green + p1.green + p2.green + p6.green + p7.green + p8.green) // 6
        avg_b = (old_p.blue + p1.blue + p2.blue + p6.blue + p7.blue + p8.blue) // 6
    elif y == (img.height-1) and (x != 0 or x != (img.width-1)):
        p1 = img.get_pixel(x - 1, y)
        p2 = img.get_pixel(x + 1, y)
        p3 = img.get_pixel(x - 1, y - 1)
        p4 = img.get_pixel(x, y - 1)
        p5 = img.get_pixel(x + 1, y - 1)
        avg_r = (old_p.red + p1.red + p2.red + p3.red + p4.red + p5.red) // 6
        avg_g = (old_p.green + p1.green + p2.green + p3.green + p4.green + p5.green) // 6
        avg_b = (old_p.blue + p1.blue + p2.blue + p3.blue + p4.blue + p5.blue) // 6
    else:
        p1 = img.get_pixel(x - 1, y)
        p2 = img.get_pixel(x + 1, y)
        p3 = img.get_pixel(x - 1, y - 1)
        p4 = img.get_pixel(x, y - 1)
        p5 = img.get_pixel(x + 1, y - 1)
        p6 = img.get_pixel(x - 1, y + 1)
        p7 = img.get_pixel(x, y + 1)
        p8 = img.get_pixel(x + 1, y + 1)
        avg_r = (old_p.red + p1.red + p2.red + p3.red + p4.red + p5.red + p6.red + p7.red + p8.red) // 9
        avg_g = (old_p.green + p1.green + p2.green + p3.green + p4.green + p5.green + p6.green + p7.green + p8.green)//9
        avg_b = (old_p.blue + p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue + p7.blue + p8.blue) // 9

    return avg_r, avg_g, avg_b


if __name__ == '__main__':
    main()
