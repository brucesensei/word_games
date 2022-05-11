# wordle
import random
from helpers import check_menu_input


with open('my_words.txt') as file:
    word_list = file.read().split('\n')

word_list = [i for i in word_list if len(i) == 5]


def print_menu():
    print('''
                        Welcome to Wordle! The world popular word guessing game. 
                        --------------------------------------------------------
        
Guess the secret 5-letter word in five attempts. Begin by typing in any 5-letter word and pressing enter.

 - Letters in the correct position of the word will show in the word.
 - Letters in the word but in the wrong postion will be shown in the word list.
 - If your guess is not in the wordle word list, you will be prompted to enter a different word with no penalty.

    Options

    1. Play
    2. Quit
''')


def definite_match(guess, word):
    '''takes word and guess as input and returns correct letter
    position matches and a list of letters in word but not correct postion.'''
    editable_word = list(word).copy()
    editable_guess = list(guess).copy()
    hidden = ['_','_','_','_','_']
    in_word = []
    not_in = set()
    for i in range(5):
        if guess[i] == word[i]:
            hidden[i] = word[i]
            editable_guess.remove(guess[i])
            editable_word.remove(guess[i])
    for letter in guess:
        if letter not in word:
            not_in.update(letter)
    for letter in editable_guess:
        if letter in editable_word:
            in_word.append(letter)
            editable_word.remove(letter)
    return hidden, in_word, not_in

def check_answer(hidden, word):
    if ''.join(hidden) == word:
        return True
    return False
      
def check_guess_input(words):
    while True:
        guess = input('Guess: ').lower()
        if guess not in word_list:
            print(f'{guess} is not in the wordle word list.')
            continue
        break
    return guess

def main():
    running = True
    while running:
        print_menu()       
        choice = check_menu_input(2)
        if choice == '2':
            running = False
        if choice == '1':
            attempts = 1
            word = random.choice(word_list)
            guesses = []
            not_in_word = set()
            while attempts < 6:
                print(f'Attempt {attempts} of 5. ', end='')
                guess = check_guess_input(word_list)
                hidden, in_word, not_in = definite_match(guess, word)
                if check_answer(hidden, word):
                    print(f'You win! the word is {word}.')
                    break
                elif not check_answer(hidden, word) and attempts == 5:
                    print(f'You loose. The word was {word}.')
                    break
                else:
                    guesses.append(guess)
                    not_in_word.update(not_in)
                    print('Guessed words: ', ', '.join(guesses))
                    print('Guessed letters that are not in the word: ', ', '.join(not_in_word))
                    print('In word but in wrong position: ', ', '.join(in_word))
                    print('Secret Word: ', ' '.join(hidden))
                    print('=======================================================')
                    print()
                    attempts += 1

if __name__ == '__main__':
    main()

            
