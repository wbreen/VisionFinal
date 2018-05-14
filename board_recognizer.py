"""
@author: William Breen

Board recognizer 

This file will take a picture,
find the gameboard in it,
create a new picture with the gameboard centered,
see if there are hits/misses on the board already,

"""

'''
Targets:
Low target:
    identify the board and center it (done)
    output the number of rows and columns (done(?))
    get the right number of squares (done)
    
Medium target:
    identify where a guess has been made(done)
    
High target:
    No longer work on a constant video feed, only on pictures of the board
    identify and weed out only the most recent guess
'''
#all needed imports
import numpy as np
import cv2
import HelpMeth as hm
import math


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
def find_b_lines(board):
    # here is a reference document: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #get image (board)
    #convert to grayscale
    g_board = hm.gray(board)
    #Blurr(?)
    g_board = hm.gaus_blur(g_board, 9)
    #get Canny edges for the given grayscale picture
    b_edge = cv2.Canny(g_board, 50, 150)
    #run cv2.HoughLines on the Canny edges you got from cv2.Canny
    board_lines = cv2.HoughLines(b_edge, 1, np.pi/180, 200)
    #
    num_lines = len(board_lines)
    for line in range(num_lines):
        for rho, theta in board_lines[line]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
        
            cv2.line(board, (x1, y1), (x2, y2), (255,255,0),2) #Draws a line on the board, so show it has been found
        
        
#    hm.showImage('board with lines drawn on', board)
    
#    game_state = [[]]
#    return game_state


'''
This method is based off of the C from aishack.in/tutorials/sudoku-grabber-opencv-detection
'''
def find_merge_lines(picture): 
    g_pic = hm.gray(picture) #make sure its grayscale
    outerbox = np.zeros(g_pic.size(), np.uint8) #create an image to put the final outer box of the playing board
    blur = hm.gaus_blur(g_pic, 11) #blur the image
    outerbox = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2) # threshold the blurred image
    cv2.bitwise_not(outerbox, outerbox)   # Invert the image, looking for the black lines
    
'''
def merge_lines(lines):
    for rho, theta in lines:
        if rho!=0 and theta !=-100:
            #determine if the line is vertical or horizontal, and do different things accordingly
            p1
            
'''

#This code comes from these two websites for finding shapes:
#https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
#https://stackoverflow.com/questions/11424002/how-to-detect-simple-geometric-shapes-using-opencv


def find_squares(board):
    copy = board.copy()

# convert the resized image to grayscale, blur it slightly,
# and threshold it
    gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    ret, thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY)
#    hm.showImage('thresh', thresh)
 
# find contours in the thresholded image and initialize the
# shape detector
    _,cnts,_ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    squares = []
    square_loc = []
    for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
        approx = cv2.approxPolyDP(c, 0.04*cv2.arcLength(c, True), True)
#        print(len(approx))
        if len(approx)==4:
#            cv2.drawContours(copy, [c], 0, (255, 0,0), -1)
            (x, y, w, h) = cv2.boundingRect(approx)
#            squares.append((x, y, x+w, y+h))
            squares.append(board[x:x+w, y:y+h])
            square_loc.append((x, y))
            cv2.rectangle(copy,(x,y),(x+w, y+h), (0,255,0),1)
#            print((x, y, x+w, y+h))
            
	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	# show the output image
#        cv2.imshow("Image", copy)
#        cv2.waitKey(0)
    return squares, square_loc, copy

#I need the size of the board
def board_size(squares):
    size = int(math.sqrt(len(squares)))
    return size

#I need a way to put the squares in a 2D array
#so this method will take the list of squares, and create a 2D numpy array to store them correctly
def align_squares_corr(squares, location, board):
    size = board_size(squares)
    aligned = np.zeros((size, size), dtype=np.uint8)
#    print(len(board[0]))
#    print(len(board[1]))
    ran_x, ran_y =int((len(board[0])/size)), int((len(board[1])/size))
    sqr_num = 0
    for (x, y) in location:
        x_cl, y_cl = False, False
#        print('x and y are', x, y)
        i=0
        while not x_cl and i<size:
            if i*ran_x-(.5*ran_x) <= x and (i+1)*ran_x-(.5*ran_x) >= x:
                j=0
                while not y_cl and j<size:
                    if j*ran_y-(.5*ran_y)  <=y and (j+1)*ran_y-(.5*ran_y)  >=y:
                        aligned[j, i] = sqr_num
#                        print('placing at', i, j)
                        y_cl=True
                    j+=1
                x_cl = True
            i+=1
        sqr_num +=1
    
    return aligned
    

#This method will find if the given square holds a dot, representing a guess by the player
#It returns true if there is a guess, and false if there isn't a guess
def find_guess(square):
    been_guessed = False
    centered = cv2.resize(square, (200, 200))
    centered = centered[25:175, 25:175]
    centered = hm.gray(centered)
    ret, thresh = cv2.threshold(centered, 100, 255, cv2.THRESH_BINARY_INV)
    #clean up the image
    size = 10
    strucEle = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, strucEle)
    _, contours, _ = cv2.findContours(close, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) >=1:
        been_guessed=True
#        hm.showImage('original square', centered)
#        hm.showImage('thresholded', close)
    return been_guessed

























