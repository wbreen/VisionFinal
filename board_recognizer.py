"""
@author: William Breen

Board recognizer 

This file will take a picture,
find the gameboard in it,
create a new picture with the gameboard centered,
see if there are hits/misses on the board already,

"""
#all needed imports
import numpy as np
import cv2
import HelpMeth as hm


#taking in the photos
imgFrom = 'grid_photos/'
two = '2x2_v2.jpg'
three = '3x3_v3.jpg'
four = '4x4_v4.jpg'
five = '5x5_v1.jpg'
seven = '7x7_v3.jpg'
ten = '10x10_v4.jpg'

#Global variables I may need
out_img_size = 500
EMPTY = 0
HIT = 1
MISS = 2

#The following code was largely based on a sudoku solver from here:
#   http://opencvpython.blogspot.com/2012/06/sudoku-solver-part-2.html
#   http://opencvpython.blogspot.in/2012/06/sudoku-solver-part-3.html

'''
This method is going to find the playing board in an image and return the board it finds centered in the image
'''
def find_playing_board(img, out_size):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #noise removal and threshold (from part 2)
    gray = cv2.GaussianBlur(gray, (15, 15), 0)
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 15, 2)
    
    #find the playing board itself (the outside edge of the board)
    #find the biggest blob in the image
        #This finds just the corners of the contour
    _,contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #This finds all the points on the contour
#    _,contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    big_blob = hm.biggest_blob(contours) #biggest blob out of all the blobs in the image (should be the board)
    
#    con_on_img = cv2.drawContours(img, big_blob, -1, (255,0,0), 50)
#    print(big_blob)
#    hm.showImage('This is where the biggest contour is in this image', con_on_img)
    
    #(From part 3)
    new_blob = hm.resize_corr(big_blob) 
    change_arr = np.array([[0,0],[out_img_size-1, 0],[0,out_img_size-1],[out_img_size-1,out_img_size-1]], np.float32)
    
    #now input array is new_blob, and desired output is change_arr
    return_val = cv2.getPerspectiveTransform(new_blob, change_arr)
    centered_board = cv2.warpPerspective(img, return_val, (out_img_size, out_img_size)) #rotate it so it is centered and correct
    
    return centered_board


'''
This method will take an image with the given playing board and identify the squares in it
It will return a 2D array that will represent if the given spot is a hit, miss, or not yet guessed (empty)
'''
def find_squares(board):
    game_state = [[]]
    return game_state