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
ex_out = 'output/'
grid_size = 500


grids = hm.read_in_files(photos)
final_boards = []
name = 1
for pic in grids:
    board = br.find_playing_board(pic, grid_size)
    final_boards.append(board)
#    hm.showImage('these are the final boards the algo found', board)
    cv2.imwrite(ex_out+'isolated'+str(name)+'.jpg', board)
    name+=1

name = 1
for board in final_boards:
    br.find_squares(board)
    cv2.imwrite(ex_out+'outlined'+str(name)+'.jpg', board)
    name+=1
    
