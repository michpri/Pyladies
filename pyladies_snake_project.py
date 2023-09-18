from random import choice #import choice function for fruit selection
from sys import exit #import exit function to exit the game

def draw_map(coordinates, fruit):
    board = [] #initalize the board as a list
    for row_n in range(height):
        row = [] #initalize the row as a list
        for column_n in range(width):
            row.append(".") #add dot to the row
        board.append(row) #add row to the board

    for piece in coordinates:
        board[piece[1]][piece[0]] = 'X' #substitute the dots with X where is present the snake body
    board[fruit[1]][fruit[0]] = 'F' #substitute the dots with F where is present the fruit
    for row in board:
        print(' '.join(row)) #join each row into a string and print    
        
def movement(): #movement function expects user input and returns updated position
    while True: 
        i = input() #asks for user input
        if i == 'w':
            new_position = (coordinates[-1][0], coordinates[-1][1]-1) #define the new head position tuple 
            if new_position not in coordinates and new_position[1] >= 0: #check that the new position is in the width or height limits and there is no another part of the snake
                coordinates.append(new_position) #append new position to coordinates list
                break
        if i == 's':
            new_position = (coordinates[-1][0], coordinates[-1][1]+1) 
            if new_position not in coordinates and new_position[1] < height: 
                coordinates.append(new_position)
                break
        if i == 'd':
            new_position = (coordinates[-1][0]+1, coordinates[-1][1])  
            if new_position not in coordinates and new_position[0] < width: 
                coordinates.append(new_position)
                break
        if i == 'a':
            new_position = (coordinates[-1][0]-1, coordinates[-1][1]) 
            if new_position not in coordinates and new_position[0] >= 0: 
                coordinates.append(new_position)
                break
        elif i=='end':
            exit() 

def new_fruit(height, width, coordinates):
    valid_positions = [] #initialize the possible fruit locations as a list
    for y in range(height):
        for x in range(width):
            if (x,y) not in coordinates: #if a tuple (x,y) is not in the coordinates
                valid_positions.append((x,y)) #add to the valid positions this tuple
    return choice(valid_positions) #return a random element of the valid_positions list

#familiriaze user with controls
intro = ("Welcome to my mini snake game!\n"
"Use following controls to feed your snake some fruits:\n"
"W for up\n"
"A for left\n"
"S for down\n"
"D for right\n"
"Good luck!\n")
print(intro) 

#define game board 5x5
width = 5
height = 5
       
coordinates = [(0,0), (0,1),(0,2)]
fruit = new_fruit(height, width, coordinates)
draw_map(coordinates, fruit)

while True: 
    movement()
    if coordinates[-1] != fruit: #if the head is not on the fruit
        coordinates.pop(0) #the last part of the body disappear
    else:
        fruit = new_fruit(height, width, coordinates) #otherwise a new fruit location is found
    
    draw_map(coordinates, fruit) #display updated game board