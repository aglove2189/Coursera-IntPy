# http://www.codeskulptor.org/#user21_WrGwe91nKrjrBDZ_0.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# initialize global variables used in your code
global random_num
global num_range
num_range = 100
global guesses
guesses = 7

# helper function to start and restart the game
def new_game():
    global random_num
    random_num = random.randrange(0, num_range)
    global guesses
    guesses = 7
    print "A new game has started, guess the number! "
    print " "


# define event handlers for control panel
def range_100():
    global num_range
    num_range = 100
    global guesses
    guesses = 7
    print "A new game will start with a range of 100."
    new_game()

def range_1000():
    global num_range
    num_range = 1000
    global guesses
    guesses = 10
    print "A new game will start with a range of 1000."
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guesses
    guesses -= 1
    
    if guesses > 0:
        if int(guess) > random_num:
            print guess + " is too high! Try again. "
            print "Guesses left: " + str(guesses)
        elif int(guess) < random_num:
            print guess + " is too low! Try again. "
            print "Guesses left: " + str(guesses)        
        else:
            print guess + " is the number, good job!"
            print " "
            new_game()
        print " "
    else:
        print "You have ran out of guesses, try again! The number was " + str(random_num) + "."
        print " "
        new_game()
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_input("Enter a guess:", input_guess, 200)
f.add_button("Range is [0, 100)", range_100, 200)
f.add_button("Range is [0, 1000)", range_1000, 200)
f.add_button("New Game", new_game, 200)

# call new_game and start frame
new_game()

# always remember to check your completed program against the grading rubric
