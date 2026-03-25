# Number Guessing game : Creating a game where the computer picks a random number and the user tries to guess it.

# Logic of program 
# Computer picks a random number between 1-10 
# User have three attempts for guess the number and user also have hint for guess the number like
# user guess higher number than real number program print a hint like (Higher number or lower number)

import random





def playGame():
    number = random.randint(1,10) # Pick a random number between 1-10
    attempt = 1
    while attempt <= 3:
        try:
            user_guess = int(input("Guess the number in 3 attempts : "))
        except ValueError:
            print("Enter a valid number")
            continue
        if user_guess > number:
            print("Your guess is higher")
        elif user_guess < number:
            print("Your guess is lower")
        else:
            print(f"Congratulation, You guess right number in {attempt}/3 attempt")
            return
        attempt += 1
    
    print(f"You could not guess the number. Right number is {number}")


def main():      
    while True:
        print("""\033[32m
            ╔╗╔╦ ╦╔╦╗╔╗ ╔═╗╦═╗  ╔═╗╦ ╦╔═╗╔═╗╔═╗  ╔═╗╔═╗╔╦╗╔═╗
            ║║║║ ║║║║╠╩╗║╣ ╠╦╝  ║ ╦║ ║║╣ ╚═╗╚═╗  ║ ╦╠═╣║║║║╣ 
            ╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═  ╚═╝╚═╝╚═╝╚═╝╚═╝  ╚═╝╩ ╩╩ ╩╚═╝
            \033[0m""")
        playGame()
        choice = input("Do you want to play again (y/n): ").lower()

        if choice == 'n':
            print("Thanks for playing")
            break
        elif choice != 'y':
            print("Enter a valid choice")
            break

if __name__ == "__main__":
    main()