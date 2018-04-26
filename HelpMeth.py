#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
William Breen
Helper methods I use in everything

"""

import numpy as np
import cv2
import glob

def showImage(winName, img):
    cv2.imshow(winName, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def gray(img):
    if len(img.shape) < 3:
        return img
    else:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def sobX_Y(img_gray):
    sob_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0)
    sob_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1)
    return sob_x, sob_y

def sob_grad_normed(img_gray):
    x, y = sobX_Y(img_gray)
    grad = np.sqrt(x**2 + y**2)
    grad = np.clip(grad, 0, 255).astype(np.uint8)
    return grad

def gaus_blur(gray_image, ker_size):
    if len(gray_image.shape[:]) > 2:
        gray_image = cv2.cvtColor(gray_image, cv2.COLOR_RGB2GRAY)
    gaussed_img = cv2.GaussianBlur(gray_image, (ker_size, ker_size), 0)
    return gaussed_img


def showSeries(winName, img):
    cv2.imshow(winName, img)
    cv2.waitKey(700)
    cv2.destroyAllWindows()

def rot_img(img, amt):
    row, col = img.shape[:2]
    center = (row//2, col//2)
    M = cv2.getRotationMatrix2D(center, -amt, 1.0)
    rotated = cv2.warpAffine(img, M, (col, row))
    return rotated

#Read in all the .jpg files from a given location and return a list
def read_in_files(loc):
    pieces = []
    pics = glob.glob(loc+'*.jpg')
    for file in pics:
        #need to have the path to the file to read it in
        file = cv2.imread(file)
        pieces.append(file)
    return pieces