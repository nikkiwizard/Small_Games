#it finally works, halellujah, praise jesus
#works fine but might lag a bit (always lagged on my chromebook)
print("Welcome To Hangman!")
print("This game is for you and a friend!")

#secret hangman word
secret_word = input("Player 1, choose a secret word with no spaces: ").lower()
#added "with no spaces" bc my code doesnt allow to guess spaces :P
#that's an issue for another day
secret_list = []
secret_list.extend(secret_word) #make a list of letters in word, for checking later

#spaces to hide word
for number in range(0,50):
  print("")

#showing the correct letters guessed
#while still having the spaces for letters not guessed
def update_spaces(secret_list, spaces, letter):
  more_spaces = ""
  for i in range(len(secret_word)): #loops through indexes
    if secret_list[i] == letter:
      more_spaces += letter #prints letter
    else:
      more_spaces += spaces[i] #prints spaces in all other indexes
  return more_spaces

#cute little ascii pictures for the game
def pictures():
  if tries == 6:
    print("-----------")
    print("|         |")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("____________")
  elif tries == 5:
    print("-----------")
    print("|         |")
    print("|         0")
    print("|")
    print("|")
    print("|")
    print("|")
    print("____________")
  elif tries == 4:
    print("-----------")
    print("|         |")
    print("|         0")
    print("|         |")
    print("|")
    print("|")
    print("|")
    print("____________")
  elif tries == 3:
    print("-----------")
    print("|         |")
    print("|         0")
    print("|         |\\")
    print("|")
    print("|")
    print("|")
    print("_____________")
  elif tries == 2:
    print("-----------")
    print("|         |")
    print("|         0")
    print("|        /|\\")
    print("|")
    print("|")
    print("|")
    print("_____________")
  elif tries == 1:
    print("-----------")
    print("|         |")
    print("|         0")
    print("|        /|\\")
    print("|          \\")
    print("|")
    print("|")
    print("_____________")
  else:
    print("-----------")
    print("|         |")
    print("|         0")
    print("|        /|\\")
    print("|        / \\")
    print("|")
    print("|")
    print("_____________")

#some variables needed for the loops
spaces = "_" * len(secret_list) #shows spaces
tries = 6 #attempts left
guesses = [] #list of letters you have already used

#loop for guessing letters in the game
while spaces != secret_word and tries > 0:
  print(pictures())
  print(f"You have tried {guesses}.")
  #loops through the indexes in spaces to print dashes/letters. updates when it goes through "update_spaces"
  for i in spaces:
    print(i, end = " ") 
  print("\n")
  print(f"You have {tries} tries left!")
  letter = input("Player 2, guess a letter!: ").lower()
  
  if len(letter) != 1: #prevent people from guessing more than 1 letter
    print("You can only guess one letter.")
  elif not letter.isalpha(): #prevent people from guessing numbers or other char
    print("You can only guess letters.")
  elif letter in guesses: #tell user if she/he already guessed the letter
    print("You already guessed that!")
  elif letter in secret_list: #this is why i made the list earlier
    print("Correct!")
    print("\n")
    spaces = update_spaces(secret_list, spaces, letter)#refers to def update_spaces
    guesses.append(letter) #adds letter to list of used letters
  else:
    print("Wrong!")
    print("\n")
    guesses.append(letter)
    tries -= 1 #minus 50 hp

#if you get all the letters and you have more than 0 tries left
#you win!
#or if you run out of tries, you lose, rip
if tries > 0:
  print("You win!!!")
  print(f"The secret word was {secret_word}.")
else:
  print("-----------")
  print("|         |")
  print("|         0")
  print("|        /|\\")
  print("|        / \\")
  print("|")
  print("|")
  print("_____________")
  print(f"You lose! The secret word was {secret_word}.")