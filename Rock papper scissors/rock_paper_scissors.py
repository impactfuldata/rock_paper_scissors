"""
This is the Rock Paper Scissors game main script 
User plays against the computer
User gets 5 goes
"""

### import modules
from supporting_class import RockPaperScissors

### initiate RockPaperScissors class
game = RockPaperScissors()

### loop to allow users 5 turns
counter = 0
while counter < 5:

### RockPaperScissors class methods for the game

# get user selection (R)ock, (P)aper, (S)cissors
    game.user_choice()

# computer selection (R)ock, (P)aper, (S)cissors   
    game.computer_choice()

# compare user and computer selection 
    game.compare_choice()

# display user selection, computer selection, user score 
    game.display()

    counter += 1