# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name: hamodi
Date: aug 7
"""
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 8

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range(4) and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for snakel  in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE
    
    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stampt = snake.stamp()
    stamp_list.append(stampt)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 50 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 350
DOWN_EDGE = -350
RIGHT_EDGE = 500
LEFT_EDGE = -550


def up():
    
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")
turtle.onkey(up, 'Up')


def left():
    global direction 
    direction=LEFT 
    print("You pressed the left key!")
turtle.onkey(left, 'Left')

def down():
    global direction 
    direction=DOWN  
    print("You pressed the down key!")
turtle.onkey(down, 'Down')


def right():
    global direction 
    direction=RIGHT 
    print("You pressed the right key!")
    
turtle.onkey(right, 'Right')

    
#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!



#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
        my_pos=(x_pos + SQUARE_SIZE, y_pos)
        
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
        my_pos=(x_pos - SQUARE_SIZE, y_pos)
        
    elif direction==DOWN:
        snake.goto(x_pos , y_pos -SQUARE_SIZE)
        print("You moved down!")
        my_pos=(x_pos , y_pos -SQUARE_SIZE)
        
    elif direction==UP:
        snake.goto(x_pos , y_pos +SQUARE_SIZE)
        print("You moved up!")
        my_pos=(x_pos , y_pos +SQUARE_SIZE)
        
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit()

    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()





    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif") 
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
x=0
food_stamps = []
for this_food_pos in food_pos:
    food.goto(food_pos[x])
    food_stamp=food.stamp()
    food_stamps.append(food.stamp)
    x=x+1
