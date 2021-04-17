from random import randint

def guessing_game():
    random_number = randint(0, 100)
    
    while True:
        try: 
            user_guess = int(input("\nGuess the number: "))
        
            if user_guess > random_number:
                print("Too high")
                 
            elif user_guess < random_number:
                print("Too low")

            elif user_guess == random_number:
                print("Just right")
                break 

        except ValueError:
            print("The entered data is not an integer.")

guessing_game() 