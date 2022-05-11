# hangman.py
from art import game_logo, running
import random
import helpers
with open('my_words.txt') as file:
    word_list = file.read().split('\n')

def check_guess(guess, word_length, display, chosen_word):
    if guess not in chosen_word:
        print(f'{guess} is not in the word.')
        return display, 1
    for position in range(word_length):
        letter = chosen_word[position]  # returns a letter in the word by index position
        if letter == guess:             # checks if guessed letter matches the letter in the word
            display[position] = letter
    return display, 0
   
def check_win_condition(display):
    if "_" not in display:
        return True 
    
def print_menu():
    print('''
    Welcome to Hangman! The classic word guessing game
    --------------------------------------------------
    
                Options
                -------
                1. Play
                2. Quit
          ''')

def get_letter_from_user(remaining_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if guess not in remaining_letters:
            print(f'{guess} is not in remaining letters. Choose a letter from the remaining letter list.')
            continue
        break
    return guess
    
stages = [
    f'''
                                  .
                                 -|-
                                  |
                              .-'~~~`-.
                            .'         `.
                            |  R  I  P  |
                            |           |
                            |           |
                            |           |
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''', '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    '''
    ]
    
def main():
    game_running = True
    while game_running:
        print(game_logo)
        print_menu()
        selection = helpers.check_menu_input(2)
        if selection == '2':
            game_running = False
        if selection == '1':            
            remaining_letters = list('abcdefghijklmnopqrstuvwxyz')
            chosen_word = random.choice(word_list)
            word_length = len(chosen_word)
            guessed_letters = []
            display = []
            for _ in range(word_length):
                display += "_"
            lives = 6
            print(f"\n{' '.join(display)}\n")
            while lives != 0:  
                guess = get_letter_from_user(remaining_letters) # guess is a single letter
                display, reducer = check_guess(guess, word_length, display, chosen_word) 
                lives = lives - reducer 
                remaining_letters.remove(guess)
                guessed_letters.append(guess) 
                print(f"\n{' '.join(display)}\n")
                print(f'Remaining Letters: {" ".join(remaining_letters)}')
                print(f'Guessed Letters: {" ".join(guessed_letters)}')
                print(stages[lives])
                print(f'Remaining Chances: {lives}')
                if lives == 0:
                    pause = input(f'The word was {chosen_word}. press any key to pay your respects and move on.')
                if check_win_condition(display):
                    print('You were lucky this time!')
                    print(f'The word was {chosen_word}.')
                    print(running)
                    pause = input('Press any key to escape.')
                    break

if __name__ == '__main__':
    main()
