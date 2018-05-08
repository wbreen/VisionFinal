"""
William Breen

Game Logic for battleship game
"""

'''
Todo in this file
Low target:
    Create gameboard (done)
    Place ships on gameboard (done)
    Guess a random spot 
    Say if given spot (from user) is a hit or a miss
    
Medium target:
    Remember where the algo has shot before, only guess in new places
    allow the user to choose the number and type of ships to play with
    
High target:
    (cheating impossible)given a guess, if it is a hit, move the ship somewhere else legal
    (cheating easy) likewise, if hit, do nothing, if miss, move a ship under that spot
'''
#import stuff
import cv2
import numpy as np
import HelpMeth as hm
import random


#Global variables
ship_types = ['Aircraft Carriers', 'Battleships','Cruisers','Submarines','Destroyers']
num_each_ship = [1, 1, 1, 2, 2]
#ships values (length)
CV=5
BB=4
CA=3
sub=2
DD=1
ship_lens = [CV, BB, CA, sub, DD]

#Untouched/miss/hit/ship defaults
miss = 1
ship = 1
hit = 2

#printing out rows
row_letters = ['A','B','C','D','E','F','G','H','I','J']


def init_game(rows, cols, debug=False, def_num_ship=False):
    ''' Need (low):
        board with ships on [default of 5 ships] (TODO)(done)
        board to guess on (TODO)
    '''
    #create boards of 0's
        #this way, 0's can be not guessed, 1's can be guesses/misses, and (later) 2's can be hits
    secret_board = np.zeros((rows, cols), dtype=np.uint8)
    guess_board = np.zeros((rows, cols), dtype=np.uint8)
    
    if not def_num_ship:
        num_each_ship = []
        for ship_type in ship_types:
            num_this_type = input("how many",ship_type, "would you like to play with? \n")
            num_each_ship.append(num_this_type)
    
    secret_board=make_secret(secret_board, num_each_ship)
    return secret_board, guess_board
    
    
#board[rows, cols]
#Here I am placing the ships on the board, and returning the modified board
def make_secret(board, num_each, debug=False):
    ship_type_looking_at=0
    for ship in num_each: #for each ship type
        for num_place in range(ship): #for the number of ships given in each ship type
            ship_len = ship_lens[ship_type_looking_at] #get the length
#            curr_board = [row[:] for row in board] #copy the current board just in case there's a mistake to go back to
            curr_board = board.copy()
            orient = random.randint(1,2) #determine if you're going to place vertically or horizontally
            
            #determine places where the ship can be placed without running over the edge
            ok_row, ok_col = len(board[0])-ship_len, len(board)-ship_len
            if debug: print('ok row and ok col are', str(ok_row), str(ok_col))
            s_row, s_col = random.randint(0, ok_row), random.randint(0, ok_col)
            
            #place horizontally
            if orient==1:
                if debug: print('placing ship horizontally')
                o=False
                while o is False:
                    board[s_row, s_col:s_col+ship_len] +=1
                    is_two = np.where(board[s_row, s_col:s_col+ship_len]>=2)
                    if debug: print(is_two[0])
                    if len(is_two[0]) >=1:#make sure you haven't placed over another ship
                        if debug: print('failed board')
                        if debug: print(board)
                        board = curr_board.copy()
                        s_row, s_col = random.randint(0, ok_row), random.randint(0, ok_col)
                        if debug: print('trying again')
                        if debug: print(board)
                    elif len(is_two[0])==0:
                        o=True
                
            #place vertically
            if orient==2:
                if debug: print('placing ship vertically')
                o=False
                while o is False:
                    board[s_row:s_row+ship_len, s_col] +=1
                    is_two = np.where(board[s_row:s_row+ship_len, s_col]>=2)
                    if debug: print(is_two[0])
                    if len(is_two[0]) >=1:#make sure you haven't placed over another ship
                        if debug: print('failed board')
                        if debug: print(board)
                        board = curr_board.copy()
                        s_row, s_col = random.randint(0, ok_row), random.randint(0, ok_col)
                        if debug: print('trying again')
                        if debug: print(board)
                        
                    elif len(is_two[0])==0:
                        o=True
        ship_type_looking_at+=1
    return board
            
#debugging/testing stuff
fake_b1 = np.zeros((10,10), dtype=np.uint8)
#fake_num1 = [1,1,1,2,2]
#print(make_secret(fake_b1, fake_num1, True))
    
def guess_shot(board, debug=False):
    rows, cols = board.shape[:2]
#    if debug: print('num rows is', rows, 'num cols is', cols)
    g_r = random.randint(0, rows-1)
    g_c = random.randint(0, cols-1)
    guess = (g_r, g_c)
    return guess


def tell_result(board, guess, debug=False):
    board[guess]+=1
    if debug: print(board)
    shot = board[guess]
    if shot == 1:
        print('miss')
    if shot >= 2:
        print('hit')
    

#more debugging stuff
#i=0
#while i<100:
#    i+=1
#    rand_guess = guess_shot(fake_b1, True)
#    tell_result(fake_b1, rand_guess, False)