import random

print(str.title("welcome to the secret number guessing game!"))

name = input("What is your name?: ")
print(f"Why hello {name}! Let's play!")
print("If you guess the secret number within five tries, you win !")

secret_number = random.randint(0,20)
tries = 1
play = "yes"
print(secret_number)

while play == "yes":
    guess = int(input("Guess a number between 0 and 20!"))
    if guess > secret_number:
        print("Too high in the sky, Try again")
        tries += 1
    elif guess < secret_number:
        print("Down low, too slow. Try again")
        tries += 1
    elif guess == secret_number:
        if tries > 5:
            print("Well you guessed right, but it took you more than 5 tries. I'm disappointed")
            play = input("Would you like to play again?(yes/no): ")
        elif tries <= 5: 
            print(f"Congrats! You win! And it only took you {tries} tries. I'm proud.") 
            play = input("Would you like to play again?(yes/no): ")

if play != "yes":
    print("Ok goodbye")