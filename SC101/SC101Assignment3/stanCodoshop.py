"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    r = pixel.red-red
    b = pixel.blue-blue
    g= pixel.green -green
    return (r**2 + g**2 + b**2)**(1/2) #color distance

def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    avg_r = 0
    avg_b = 0
    avg_g = 0
    for pixel in pixels:
        avg_r += pixel.red
        avg_g += pixel.green
        avg_b += pixel.blue
    rgb= [int(avg_r/len(pixels)),int(avg_g/len(pixels)),int(avg_b/len(pixels))]
    return rgb

def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """

    avg = get_average(pixels)
    best_distance = 255*3 #r&g&b max =255 /maximum distance = 255*3
    best_point = None
    for pixel in pixels:
        next_pixel_distance = get_pixel_dist(pixel,avg[0],avg[1],avg[2])
        if  next_pixel_distance < best_distance:
            best_distance = next_pixel_distance
            best_point = pixel
    return best_point

def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):
        for y in range(height):
            images_pixel =[] #reset the list on every pixel
            for image in images: #input all the pics
                pixel = image.get_pixel(x, y)
                images_pixel.append(pixel) #record the pixel (x,y)
                new_pixel = result.get_pixel(x, y)
                new_pixel.red =get_best_pixel(images_pixel).red
                new_pixel.green = get_best_pixel(images_pixel).green
                new_pixel.blue = get_best_pixel(images_pixel).blue



    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
