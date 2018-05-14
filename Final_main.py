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
squares, _,_ = br.find_squares(board)
size = br.board_size(board)
secret_board, guess_board = g_log.init_game(size, size, _, True)
#identify if there are any marks on the board (hit or miss)
for s in squares:
    is_guessed = br.find_guess(s)
#guess a spot to shoot
spot = g_log.guess_shot(guess_board)
#show an image of where you want to shoot and print out this location [e5, c2, etc] (somehow)


