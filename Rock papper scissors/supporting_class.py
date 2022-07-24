"""
This script contains the supporting class needed by the Rock Paper Scissors main script 
"""

### import modules
import sys
import random

### create class
class RockPaperScissors():
    """
    Class for playing the Rock Paper Scissors game

    User is welcomed to game
    User selection (R)ock, (P)aper, (S)cissors is obtained
    Computer selection (R)ock, (P)aper, (S)cissors is made
    User and computer selection is compared
    User selection, Computer selection, User score is displayed
    """
    
    def __init__(self):
        """
        User is welcomed to game
        """

        ### provide game instructions to users
        print("""
              Welcome to this Rock, Paper, Scissors Game
              You will play against the computer
              You get 5 goes
              Let's see the score you can get  
              """)
        
        ### get user choice to play the game 
        self.play_choice = input("If you would like to play this game, type Y: ")

        ### exit the script if users don't want to play
        if self.play_choice != "Y":
            sys.exit()
        
        ### if users want to play initiate their score
        else:
            self.user_score = 0

    def user_choice(self):
        """
        User selection (R)ock, (P)aper, (S)cissors is obtained
        """
        
        ### loop until users provide a valid input: R, P, or S
        while True:
            self.user_selection = input("""\nType R for Rock or Type P for Paper or Type S for Scissors """)
            if self.user_selection == "R" or self.user_selection == "P" or self.user_selection == "S" :
                break
            else:
                print("Your input is invalid. Please, try again\n")

    def computer_choice(self):
        """
        Random computer selection (R)ock, (P)aper, (S)cissors is made
        """
        
        self.computer_selection = random.choice(["R", "P", "S"])

    def compare_choice(self):
        """
        User and computer selection is compared
        """
        
        ### compare when user selection is R
        if self.user_selection == "R" and self.computer_selection == "R":
            self.user_score += 0
        elif self.user_selection == "R" and self.computer_selection == "P":
            self.user_score += -1
        elif self.user_selection == "R" and self.computer_selection == "S":
            self.user_score += 1
       
        ### compare when user selection is P
        elif self.user_selection == "P" and self.computer_selection == "P":
            self.user_score += 0
        elif self.user_selection == "P" and self.computer_selection == "S":
            self.user_score += -1
        elif self.user_selection == "P" and self.computer_selection == "R":
            self.user_score += 1

        ### compare when user selection is S
        elif self.user_selection == "S" and self.computer_selection == "S":
            self.user_score += 0
        elif self.user_selection == "S" and self.computer_selection == "R":
            self.user_score += -1
        elif self.user_selection == "S" and self.computer_selection == "P":
            self.user_score += 1

    def display(self):
        """
        display user selection, computer selection, user score
        """
        
        print (f"user selection: {self.user_selection}, computer selection: {self.computer_selection}, user score: {self.user_score}\n")
