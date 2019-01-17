#it works hallelujah praise jesus amirite
import random
import time

#here's my dictionaries
game_wins = {
  "rock_wins": {
    "scissors": "crushes",
    "lizard": "crushes",
  },
  "paper_wins": {
    "rock": "covers",
    "spock": "disproves"
  },
  "scissors_wins":{
    "paper": "cuts",
    "lizard": "decapitates",
  },
  "lizard_wins": {
    "spock": "poisons",
    "paper": "eats",
  },
  "spock_wins": {
    "scissors": "smashes",
    "rock": "vaporizes",
  }
}
game_losses = {
  "rock_loses": {
    "spock": "vaporizes",
    "paper": "covers",
  },
  "paper_loses": {
    "scissors": "cuts",
    "lizard": "eats",
  },
  "scissors_loses": {
    "spock": "smashes",
    "rock": "smashes",
  },
  "lizard_loses": {
    "scissors": "decapitates",
    "rock": "crushes",
  },
  "spock_loses": {
    "paper": "disproves",
    "lizard": "poisons",
  }
}

#here's my dramatic greeting
print("Welcome to Rock,")
time.sleep(.75)
print("Paper!")
time.sleep(.75)
print("Scissors!")
time.sleep(.75)
print("LIZARD!")
time.sleep(.75)
print("SPOCK!")
print("First one to 3 wins!")
print("You have 2 attempts to beat the computer")

#my list of viable options to choose from
options = ["rock", "paper", "scissors", "lizard", "spock"]

def player_choice():
  '''Get input from the user's decision'''
  choice = input("Choose your fighter: ").lower()
  if choice in options:
    return choice
  else:
    print("That's not an option, I'm disappointed")

def computer_choice():
  '''Get the computer's randomized decision'''
  choice = random.choice(options)
  return choice

#variables for how many wins each has
player_wins = 0
computer_wins = 0

#dont mind me defining some functions
def play():
  '''Play the main game and see who wins'''
  global player_wins
  global computer_wins
  player = player_choice()
  computer = computer_choice()
  print("computer chose...")
  time.sleep(1)
  print(computer.upper())
  print("\n")
  if player == computer:
    print("Tie! Try Again!")
  elif player == "rock":
    if computer in game_wins["rock_wins"]:
      print("You Win!")
      print("ROCK", game_wins["rock_wins"][computer], computer, ".")
      player_wins += 1
    else:
      print("You Lose!")
      print(computer.upper(), game_losses["rock_loses"][computer], player, ".")
      computer_wins +=1
  elif player == "paper":
    if computer in game_wins["paper_wins"]:
      print("You Win!")
      print("PAPER", game_wins["paper_wins"][computer], computer, ".")
      player_wins += 1
    else:
      print("You Lose!")
      print(computer.upper(), game_losses["paper_loses"][computer], player, ".")
      computer_wins += 1
  elif player == "scissors":
    if computer in game_wins["scissors_wins"]:
      print("You Win!")
      print("SCISSORS", game_wins["scissors_wins"][computer], computer, ".")
      player_wins += 1
    else:
      print("You Lose!")
      print(computer.upper(), game_losses["scissors_loses"][computer], player, ".")
      computer_wins += 1
  elif player == "lizard":
    if computer in game_wins["lizard_wins"]:
      print("You Win!")
      print("LIZARD", game_wins["lizard_wins"][computer], computer, ".")
      player_wins += 1
    else:
      print("You Lose!")
      print(computer.upper(), game_losses["lizard_loses"][computer], player, ".")
      computer_wins += 1
  elif player == "spock":
    if computer in game_wins["spock_wins"]:
      print("You Win!")
      print("SPOCK", game_wins["spock_wins"][computer], computer, ".")
      player_wins += 1
    else:
      print("You Lose!")
      print(computer.upper(), game_losses["spock_loses"][computer], player, ".")
      computer_wins += 1
  else:
    print("That's not one of the options")

def display_score():
  '''How many times has each player won?'''
  print("\n")
  print(f"Player has won {player_wins} times.")
  print(f"Computer has won {computer_wins} times.")

#combines play() and display_score() and determines when someone wins
def game():
  '''determining who wins'''
  '''this was mostly to make my life easier and loop it again later'''
  while player_wins != 3 and computer_wins != 3:
    play()
    display_score()
    
  if player_wins == 3:
    print("\n")
    print("Congrats! You Won!")
  elif computer_wins == 3:
    print("\n")
    print("Sorry, the computer beat you :/")

#run the game lol
game()

#would you like to play again ?
again = input("Would you like to try again?: ").lower()
if again == "yes" or again == "y":
  computer_wins = 0
  player_wins = 0
  game()
else:
  print("Ok thanks for playing")