#Weekly Challenge 2
#Thomas West

#Import the random module
import random

#Create a list of Pokemon types
pokemon = ["Water", "Fire", "Grass"]
#Create a random generator
computer = random.choice(pokemon)
#Ask the user to input a Pokemon type
user = input("Select your Pokemon type of either Water, Fire, or Grass: ")
user = user.lower()
#User inputs water type 
if user == 'water':
    #Computer chooses fire type
    if computer == 'Fire':
        print("You chose Water")
        print("Computer chose Fire")
        #User wins
        print("Congratulations! Your Pokemon won!")
    #Computer chooses grass type
    elif computer == 'Grass':
        print("You chose Water")
        print("Computer chose Grass")
        #Computer wins
        print("Sorry. Your Pokemon lost.")
    #Computer chooses water type
    elif computer == 'Water':
        print("You chose Water")
        print("Computer chose Water")
        #Draw
        print("It's a draw.")
#User inputs fire type
if user == 'fire':
    #Computer chooses fire type
    if computer == 'Fire':
        print("You chose Fire")
        print("Computer chose Fire")
        #Draw
        print("It's a draw.")
    #Computer chooses grass type
    elif computer == 'Grass':
        print("You chose Fire")
        print("Computer chose Grass")
        #User wins
        print("Congratulations! Your Pokemon won!")
    #Computer chooses water type
    elif computer == 'Water':
        print("You chose Fire")
        print("Computer chose Water")
        #Computer wins
        print("Sorry. Your Pokemon lost.")
#User inputs grass type
if user == 'grass':
    #Computer chooses fire type
    if computer == 'Fire':
        print("You chose Grass")
        print("Computer chose Fire")
        #Computer wins
        print("Sorry. Your Pokemon lost.")
    #Computer chooses grass type
    elif computer == 'Grass':
        print("You chose Grass")
        print("Computer chose Grass")
        #Draw
        print("It's a draw.")
    #Computer chooses water type
    elif computer == 'Water':
        print("You chose Grass")
        print("Computer chose Water")
        #User wins
        print("Congratulations! Your Pokemon Won!")
