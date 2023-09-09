#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 22:51:37 2022

@author: arihantpandey
"""
"""
CONNECT 4
GAME DIMENSIONS 6 rows, 7 columns



"""
#from graphics import *


class game_c4:
    #rack = [][]
    
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.rack = [['O']*self.rows for i in range(self.columns)]
        #self.rack[column][row]
        
        self.play_game()
        
    
    def valid_move(self, col):
        #check if the chosen column is full
        if(self.rack[col-1][-1]=='O'):
            return True
        return False
        
    def add_piece(self, col, turn):
        #add piece of correct color to column
        if turn%2:
            for i in range(self.rows):
                if(self.rack[col-1][i] == 'O'):
                    self.rack[col-1][i] = "R"
                    break
        else:
            for i in range(self.rows):
                if(self.rack[col-1][i] == 'O'):
                    self.rack[col-1][i] = "Y"
                    break
            
    def check_win(self, rack, symbol):
        #check for horizontal c4
        for y in range(len(self.rack[0])):
            for x in range(len(self.rack) - 3):
                if rack[x][y] == symbol and rack[x+1][y] == symbol and rack[x+2][y] == symbol and rack[x+3][y] == symbol:
                    return True       
        #check for vertical c4
        for y in range(len(self.rack[0])-3):
            for x in range(len(self.rack)):
                if rack[x][y] == symbol and rack[x][y+1] == symbol and rack[x][y+2] == symbol and rack[x][y+3] == symbol:
                    return True
        #check for diagonal c4
        for y in range(len(self.rack[0])-3):
            for x in range(len(self.rack)-3):
                if rack[x][y] == symbol and rack[x+1][y+1] == symbol and rack[x+2][y+2] == symbol and rack[x+3][y+3] == symbol:
                    return True
        return False
        
    def display_rack(self):
        #print("display not ready yet")
        print()
        for j in range(-1, -1*self.columns, -1):
            for i in range(0, 1*self.rows+1, 1):
                print(self.rack[i][j], end = ' ')
            print()
        print()
        #print(self.rack)
        
    def end(self):
        print()
        print()
    
        ng = input("If you would like to start a new game press y: ")
        if(ng == "y"):
            flag = 0
            while flag == 0:
                try:
                    r = int(input("number of rows: "))
                    flag = 1
                except ValueError:
                    flag = 0
            while flag == 1:
                try:
                    c = int(input("number of columns: "))
                    flag = 2
                except ValueError:
                    flag = 1
            self.__init__(r,c)
    def play_game(self):
        print("Let's play Connect 4!")
        print("Player 1, you have the red pieces. Player 2 you have the yellow pieces.")
        
        for turn in range(1, self.rows*self.columns+1):
            col = -1
            next_turn = 0
            
            
            while(next_turn == 0):
                flag = 0
                while(flag == 0):
                    try:
                        col = int(input(f"Move {turn}: Please choose a valid column from 1 to {self.columns}: "))
                        if(0 < col <= self.columns):
                            flag = 1
                    except ValueError:
                        flag = 0
                        
                
                if(self.valid_move(col)):
                    self.add_piece(col, turn)
                    self.display_rack()
                    if self.check_win(self.rack, "R"):
                        print("red won!") 
                        self.end()
                    if self.check_win(self.rack, "Y"):
                        print("yellow won!") 
                        self.end()
                    
                    next_turn = 1
                else:
                    print("that column is full")
                    col = -1
                        

g = game_c4(6,7)