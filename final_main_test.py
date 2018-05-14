"""
William Breen

Computer Vision Final Project
This is a dummy file for testing things
"""

import cv2
#import numpy
import HelpMeth as hm
import game_logic as g_log
import board_recognizer as br

photos = 'grid_photos/'
guesses = 'grid_guesses/'
two = '2x2_v2.jpg'
three = '3x3_v2.jpg'
four = '4x4_v4.jpg'
five = '5x5_v1.jpg'
seven = '7x7_v3.jpg'
ten = '10x10_v4.jpg'

#game guesses
new_board=photos+'2x2v1.jpg'
one_g = guesses+'one_g_2x2.jpg'
two_g = guesses+'two_g_2x2.jpg'
three_g = guesses+'three_g_2x2.jpg'
four_g = guesses+'four_g_2x2.jpg'

ex_out = 'output/'
grid_size = 500
debug = False

'''
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
    '''

'''
board = cv2.imread(guesses+'sixteen_g_10x10.jpg')
board = br.find_playing_board(board, grid_size)
squares, loc, final = br.find_squares(board)
#hm.showImage('squares identified', final)
num_g=0
for i in squares:
    guess = br.find_guess(i)
    if guess:
        num_g+=1
print(str(num_g))
#print(len(squares))
images_aligned = br.align_squares_corr(squares, loc, final)
'''
#print(images_aligned)

def play_game(start_pic, start):
    #is the game over yet?
    game_over = False
    board = br.find_playing_board(start_pic, grid_size)
    squares, loc, final = br.find_squares(board)
    size = br.board_size(squares)
    if start:
        sec_board, g_board = g_log.init_game(size, size, debug, True)
        start = False
    print('the secret board is', sec_board)
    print('the guess board is', g_board)
    
#    if
    return game_over





'''
What do I need to be persistent through the loops:
    the state of the guesses 
    state of my secret board


How to tell when the game is over:
    all the squares have been guessed
    all the boats are sunk
    
'''







#
#
#while not game_over:
#    game_over = play_game()
#












