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
new_board=photos+'2x2_v1.jpg'
one_g = guesses+'one_g_2x2.jpg'
two_g = guesses+'two_g_2x2.jpg'
three_g = guesses+'three_g_2x2.jpg'
four_g = guesses+'four_g_2x2.jpg'

short_game = []
short_game.append(new_board)
#hm.showImage('file', short_game[0])
short_game.append(one_g)
short_game.append(two_g)
short_game.append(three_g)
short_game.append(four_g)

short_game1=[]
for game in short_game:
    g_file = cv2.imread(game)
    short_game1.append(g_file)
#    hm.showImage('file', g_file)



ex_out = 'output/'
grid_size = 500
debug = False
start = True

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


board = cv2.imread(guesses+'sixteen_g_10x10.jpg')
board = br.find_playing_board(board, grid_size)
squares, loc, final = br.find_squares(board)
hm.showImage('squares identified', final)
num_g=0
for i in squares:
    guess = br.find_guess(i)
    if guess:
        num_g+=1
print(str(num_g))
#print(len(squares))
images_aligned = br.align_squares_corr(squares, loc, final)

#print(images_aligned)
'''
def play_game(start_pic, start, sec_board, g_board):
    #is the game over yet?
    game_over = False
    board = br.find_playing_board(start_pic, grid_size)
    squares, loc, final = br.find_squares(board)
    size = br.board_size(squares)
    if start:
        sec_board, g_board = g_log.init_game(size, size, debug, True)
        start = False
    
#        print('the secret board is \n', sec_board)
#        print('the guess board is \n', g_board)
    if not start:
        print('the secret board is \n', sec_board)
        print('the guess board is \n', g_board)
        aligned_squares = br.align_squares_corr(squares, loc, board)
        print(aligned_squares)
        place = 0
        for x in squares:
            hm.showImage('square', x)
            is_guessed = br.find_guess(x)
            print(loc[place])
            if is_guessed:
                for i in aligned_squares:
                    for j in aligned_squares[0]:
                        print(aligned_squares[j])
                        if aligned_squares[i,j] == squares[x]:
                            
#                x,y = aligned_squares[place]
                            g_log.tell_result(sec_board, (i,j))
            place+=1
#            for y in aligned_squares[0]:
#                
#                print(y)
#                sqr_num = squares[y]
##                hm.showImage('test', final)
#                is_guessed = br.find_guess(squares[sqr_num])
##                print(str(x))
##               is_guessed = br.find_guess(squares[x])
#                if is_guessed:
#                    g_log.tell_result(sec_board, (x,y))
        
    
    return game_over, sec_board, g_board

'''



'''
What do I need to be persistent through the loops:
    the state of the guesses 
    state of my secret board


How to tell when the game is over:
    all the squares have been guessed
    all the boats are sunk
    
'''

#
#sec_board = [[]]
#g_board = [[]]
#for state in short_game1:
#    _, sec_board, g_board = play_game(state, start, sec_board, g_board)
#    start=False
#    cv2.imshow('current board state', state)



#
#
#while not game_over:
#    game_over = play_game()
#












