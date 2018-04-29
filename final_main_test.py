"""
William Breen

Computer Vision Final Project
This is a dummy file for testing things
"""

#import cv2
#import numpy
import HelpMeth as hm
#import game_logic as g_log
import board_recognizer as br

photos = 'grid_photos/'
grid_size = 500 

grids = hm.read_in_files(photos)
final_boards = []

for pic in grids:
    board = br.find_playing_board(pic, grid_size)
    final_boards.append(board)
    #hm.showSeries('these are the final boards the algo found', board)

