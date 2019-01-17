import random
import time

class Character:
  """Generic character class"""
  
  def __init__(self,name):
    self.name = name
    self.health = 50
    
  def display(self):
    print(f"{self.name} has:")
    print(f"- {self.health} health points")
    print(f"- {self.defense} defense points")
    print(f"- {self.attack} attack points")
    
  def fight(self,target):
    print(f"{target.name} has {target.health} health points left!")
    chance = [0,1]
    luck = random.choice(chance)
    print(f"{self.name} attacks!")
    print("\n")
    time.sleep(1)
    if luck == 1:
      print(f"{self.name}'s attack succeeds!")
      target.health -= self.attack
      print(f"{target.name} drops to {target.health} health.")
    else:
      print(f"{self.name}'s attack misses!")
      print(f"{target.name} loses no health")

  def defend(self,target):
    atk = int(1.3 * target.attack)
    print("Computer attacks!")
    time.sleep(1)
    if atk > self.defense:
      self.health -= atk
      print(f"Computer's attack was too strong! You lose {atk} health points")
      print(f"Health is now down to {self.health}")
    else:
      print("No damage taken")
      print(f"Health points still at {self.health}")

class Player(Character):
  """Class for a player character"""
  
  def __init__(self,name):
    Character.__init__(self,name)
    self.attack = 25
    self.defense = 20

  def flee(self):
    print(f"{self.name} decides to flee the fight!")

  def special_attack(self,target):
    self.attack += 20
    player.fight(target)
    self.attack -= 20

class Opponent(Character):
  """Class for opponents"""

  def __init__(self, name):
    Character.__init__(self,name)
    self.attack = 20
    self.defense = 25
  
  def heal(self):
    time.sleep(1)
    self.health += 10
    print(f"{self.name} has used a healing potion!")
    print(f"{self.name} now has {self.health} health")

name = input("USER! What is your name?: ")

player = Player(name)
computer = Opponent("Computer")

print(f"Welcome, Agent {name}.")
print("Your goal is to defeat the computer. Good luck Agent.")
print("\n")

print("Here are your stats:")
player.display()
print("\n")

player_options = ["Display", "Fight", "Defend", "Flee", "Special Attack"]
computer_options = ["fight", "heal"]

print(player_options)
print("These are your options to defend the world.")
print("The special attack may only be used once")

special_atk_list = []

def player_choice():
  print("\n")
  choice = input("Make your selection: ").lower()
  if choice == "fight":
    player.fight(computer)
  elif choice == "defend":
    player.defend(computer)
  elif choice == "flee":
    print("COWARD. No fleeing allowed.")
  elif choice == "display":
    player.display()
  elif choice == "special attack":
    if "special attack" in special_atk_list:
      print("You already used the special attack")
    else:
      player.special_attack(computer)
      special_atk_list.append("special attack")
  else:
    print("AGENT! That isn't one of the options!")

def computer_choice():
  choice = random.choice(computer_options)
  if choice == "fight":
    computer.fight(player)
  elif choice == "defend":
    computer.defend(player)
  elif choice == "heal":
    computer.heal()

while player.health >= 0 and computer.health >= 0:
  player_choice()
  print("\n")
  computer_choice()

print("\n")
if player.health <= 0:
  print("Mission failed, agent. Better luck next time")
elif computer.health <= 0:
  print("MISSION SUCCESS!")
  print(f"Well Done, Agent {name}")
  print("The world is saved thanks to you")