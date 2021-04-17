from random import randint

def guessing_game():
    random_number = randint(0, 100)
    
    for count in range(5):
        try: 
            user_guess = int(input("\nGuess the number: "))
        
            if user_guess > random_number:
                print("Too high")
                 
            elif user_guess < random_number:
                print("Too low")

            elif user_guess == random_number:
                print("Just right")
                break 
            
            if count == 4:
                print("\nSorry! You did not guess that.")
                exit(0)
        
        except ValueError:
            print("The entered data is not an integer.")
    
    print(f"The number was {random_number}")


guessing_game() 