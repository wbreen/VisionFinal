"""
William Breen

Computer Vision Final Project

Detecting and playing a game of hand-drawn Battleship on a grid
"""

import cv2
import numpy
import HelpMeth as hm
import game_logic as g_log
import board_recognizer as br

#read in image that the board is in
boards = 'grid_photos/'
grid_size = 500
grids = hm.read_in_files(boards)
final_boards = []

#identify the board (need an output size)
for g in grids:
    board = br.find_playing_board(g, grid_size)
    final_boards.append(board)
board = final_boards[1]
#identify the squares in the board (Hough lines?)

#identify if there are any marks on the board (hit or miss)

#guess a spot to shoot

#show an image of where you want to shoot and print out this location [e5, c2, etc] (somehow)

#need way to indicate to computer if sunk

