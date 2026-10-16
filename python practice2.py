import random
#here i have imported the random module to use randint later on
def user_random_number():
    while True:
#here i have used def to define the user's inputted number and while true to create a loop
        try:
            return int(input("Enter a number: "))
#here the user can input a number and the script will use this to guess the number
        except ValueError:
#except used to prevent the program from crashing if the user inputs a letter or word instead of a number
            print("Hey! numbers only")
while True:
    result = user_random_number()
    print("Now I'm going to guess your number, is your number", result, "?")
    while True:
        guess_check = input("yes/no: ").lower().strip()
        if guess_check == "yes":
            print("Nice! I guessed your number")
            break
        elif guess_check == "no":
            print("Whoops wrong guess")
            break
        else:
            print("Please enter yes or no only")
#above is a a if, elif and else statement to check if the user has inputted yes or no and if not it will prompt them to enter yes or no only
    while True:
        print("Now with that over should i randomise your number for fun?")
        choice = input("yes/no: ").lower().strip()
        if choice == "yes":
            random_number = random.randint(1, 10)
#here the imported random module is used to randomise the user's number and the user can guess it afterwards
            print("There, now I've randomised your number between 1 and 10 and I want you to guess it!")
            while True:
                try:
                    guess = int(input("Enter your guess: "))
                except ValueError:
                    print("Hey! numbers only")
                    continue
                if guess > random_number:
                    print("Too high, try again")
                elif guess < random_number:
                    print("Too low, try again")
                else:
                    print("That's correct!, the random number was", random_number, "!")
                    break
            break
        elif choice == "no":
            print("Another time then")
            break
        else:
            print("Enter yes or no only")

    if input("Go again? yes/no: ").lower().strip() != "yes":
        print("see you next time")
#final part of the scrip that allows the user to go again or exit the program
    else:
        continue
    break