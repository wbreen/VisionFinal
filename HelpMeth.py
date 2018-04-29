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


#For the battleship game: given contours and a hierarchy, return the largest blob
    #This code was taken from here: http://opencvpython.blogspot.com/2012/06/sudoku-solver-part-2.html
def biggest_blob(contours):
    biggest = None
    max_area = 0
    for con in contours:
        area = cv2.contourArea(con)
        if area > 100:
            peri = cv2.arcLength(con, True)
            approx = cv2.approxPolyDP(con, 0.02*peri, True)
            if area > max_area and len(approx)==4:
                biggest = approx
                max_area = area
    return biggest
    
    
#Resize the 4 corners of the game board in array like [t-left, t-right, b-left, b-right]
#Code from part 3: http://opencvpython.blogspot.in/2012/06/sudoku-solver-part-3.html
def resize_corr(b_corners):
    b_corners = b_corners.reshape((4, 2))
    new_corners = np.zeros((4, 2), dtype = np.float32)
    #reorder the points of the blob from random to t-left, t-right, b-left, b-right
    #with x,y coorinates: y+x: t-left is smallest sum, b-right is max sum (of both)
    #with x,y coords: y-x: t-right is minimum, b-left is max
    add = b_corners.sum(1)
    new_corners[0] = b_corners[np.argmin(add)] #top left corner
    new_corners[3] = b_corners[np.argmax(add)] #bottom right corner
    diff = np.diff(b_corners, axis = 1)
    new_corners[1] = b_corners[np.argmin(diff)] #top right corner
    new_corners[2] = b_corners[np.argmax(diff)] #bottom left corner
    
    return new_corners






