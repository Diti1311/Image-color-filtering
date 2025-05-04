
import cv2
import numpy as np
from tkinter import filedialog, Tk


def red_filter(image):
    image[:, :, 1] = 0
    image[:, :, 0] = 0
    return image

def green_filter(image):
    image[:, :, 2] = 0
    image[:, :,0] = 0
    return image

def blue_filter(image):
    image[:, :,2] = 0
    image[:, :,1] = 0
    return image

def main():
    Tk().withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    image = cv2.imread(file_path)

    if image is None:
        print("Failed to load image.")
    else:
        new_dimensions= (500,500)
        image = cv2.resize(image , new_dimensions)
        cv2.imshow("Uploaded Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    filter = 0
    while filter!=5:
        filter = int(input('Enter the number to convert the image to: \n1.Grayscale\n2.Red filter\n3.Green Filter\n4.Blue filter\n5.exit : '))
        if filter == 1:
            gray_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
            cv2.imshow('Grayscale Image', gray_image)
        if filter == 2:
            red_filtered = red_filter(image.copy())
            cv2.imshow('Red Filter',red_filtered)
        if filter == 3:
            green_filtered = green_filter(image.copy())
            cv2.imshow('Green Filter',green_filtered)

        if filter == 4:
            blue_filtered = blue_filter(image.copy())
            cv2.imshow('Blue Filter',blue_filtered)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
main()
