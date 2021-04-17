from random import randint, choice
from textwrap import dedent


def guessing_game():
    while True:
        print(dedent('''\n
            1. Number
            2. Word
        \n'''))    
        user_option = int(input("Choose the game: "))
        
        if user_option == 1:
            guess_number()
        
        elif user_option == 2:
            guess_word()
        
        else:
            print("\nEnter the option correctly, please.")

# Guess the number chosen between 1 and 100 to see if it's true
def guess_number():
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

# Guess a word from the list to see if it's true
def guess_word():
    word_list = ['pythonic', 'unittest', 'fstring', 'number', 'manning', 'book', 'exercise']
    random_word = choice(word_list)

    for word_count in range(5):
        try:
            user_word_guess = input("\nGuess the word: ")

            if user_word_guess < random_word:
                print("Go further in dictionary")

            elif user_word_guess > random_word:
                print("Come nearer in dictionary")

            else:
                print("That's it!")
                break

            if word_count == 4:
                print("Sorry! You could not guess the word!")        
        
        except TypeError:
            print("Enter yoyr guess correctly, please.")


guessing_game()