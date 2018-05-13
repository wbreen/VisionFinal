"""
William Breen

Computer Vision Final Project
This is a dummy file for testing things
"""

import cv2
#import numpy
import HelpMeth as hm
#import game_logic as g_log
import board_recognizer as br

photos = 'grid_photos/'
guesses = 'grid_guesses/'
two = '2x2_v2.jpg'
three = '3x3_v2.jpg'
four = '4x4_v4.jpg'
five = '5x5_v1.jpg'
seven = '7x7_v3.jpg'
ten = '10x10_v4.jpg'

ex_out = 'output/'
grid_size = 500


grids = hm.read_in_files(photos)
final_boards = []
name = 1
for pic in grids:
    board = br.find_playing_board(pic, grid_size)
    final_boards.append(board)
#    hm.showImage('these are the final boards the algo found', board)
#    cv2.imwrite(ex_out+'isolated'+str(name)+'.jpg', board)
#    name+=1

name = 1
for board in final_boards:
#    br.find_b_lines(board)
#    hm.showImage('board with lines on', board)
#    cv2.imwrite(ex_out+'outlined'+str(name)+'.jpg', board)
#    name+=1
    squares, board = br.find_squares(board)
    hm.showSeries('squares found', board)
    print("the number of squares found was " +str(len(squares)))
    




#board = cv2.imread(photos+three)
#board = br.find_playing_board(board, grid_size)
#squares = br.find_squares(board)
#print(len(squares))




