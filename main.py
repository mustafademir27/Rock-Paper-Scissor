#Import the random library
import random

#create a list containing the three actions of the game.
list_game = ["rock","paper","scissor"]

#Set the scores of players to 0
point_player = 0
point_computer = 0

#Ask the user how many rounds they want to play
round = int(input("How many rounds do you want to play = "))

#Add a round_counter that is 0 at the beginning
round_counter = 0

#Write a while loop and put the game inside
while True:  

  #Increase round_counter by and print it
  round_counter +=1
  print(f"\n{round_counter}. round started.\n")

  #Select a random action for computer
  action_computer = random.choice(list_game)

  #Ask player to choose an action
  action_player = str(input("rock paper scissor ? = "))
  #Print the players choices
  print("Computer's choice = ",action_computer)
  print("Player's choice = ",action_player)

  #tie condition
  if action_player == action_computer:
    print("Tie!")

  #Remaining conditions
  elif action_player == "rock" and action_computer == "scissor":
    print(f"{round_counter}. round player won.\n")
    point_player += 1
    print(f"Player = {point_player}\nComputer = {point_computer}")

  elif action_player == "rock" and action_computer == "paper":
    print(f"{round_counter}. round computer won.\n")
    point_computer += 1
    print(f"Player = {point_player}\nComputer = {point_computer}")

  elif action_player == "paper" and action_computer == "scissor":
    print(f"{round_counter}. round computer won.\n")
    point_computer += 1
    print(f"Player = {point_player}\nComputer = {point_computer}")

  elif action_player == "paper" and action_computer == "rock":
    print(f"{round_counter}. round player won.\n")
    point_player += 1
    print(f"Player = {point_player}\nComputer = {point_computer}")

  elif action_player == "scissor" and action_computer == "paper":
    print(f"{round_counter}. round player won.\n")
    point_player += 1
    print(f"Player = {point_player}\nComputer = {point_computer}")

  elif action_player == "scissor" and action_computer == "rock":
    print(f"{round_counter}. round computer won.\n")
    point_computer += 1
    print(f"Player = {point_player}\nComputer = {point_computer}")


  #Stop the while loop if the round_counter equals the number of total rounds
  if round_counter == round:
    break


#Print the outcome of the game by using conditional statements
if point_computer > point_player:
  print("Computer won.")
elif point_computer < point_player:
  print("Player won.")
else:
  print("Tie. None won.")
