# countdown

#================================imports==========================================
import random
import time
from helpers import check_menu_input
#================================Constants========================================

# consonants = string of consonants
# vowels = string of vowels
# word_list = somewhat comprehensive list of english words.
# conundrum_list = a list of 9-letter words derived from word_list

with open('my_words.txt') as file:
    word_list = file.read().split('\n')

conundrum_list = [i for i in word_list if len(i) == 9]
consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'

#===========================main game logic========================================

def get_letters(vowels, consonants):
    '''Allows the user to choose a ramdomly generated consonant or vowel to populate
    a 9-letter list of letters.'''
    letters = []
    for i in range(9):
        selection = input('Choose "v" for a vowel or any other key for a consonant. ')
        if selection == 'v':
            letters.append(random.choice(vowels))
            print(', '.join(letters))
        else:
            letters.append(random.choice(consonants))
            print(', '.join(letters))
    return letters

def possible_words(word_list, letter_list):
    '''Checks all words in the word_list against letters in the letter_list
    and returns all words that can be constructed from the letters in letter_list.'''
    valid_words = []
    for word in word_list:
        word_copy = list(word)
        letter_list_copy = letter_list.copy()
        for letter in word:
            if letter in letter_list_copy:
                word_copy.remove(letter)
                letter_list_copy.remove(letter)
        if not word_copy:
            valid_words.append(word)
    return valid_words

def counter(manual=False, count=30):
    '''counts down from 30. If manual set to false, countdown begins automatically. '''
    if manual:
        start = input('Press any key to start the countdown. ')
    for i in range(count):
        print(count,', ', end='')
        count -= 1
        time.sleep(1)
        
def format_letters(letter_list):
    print(f'''
          
          .----------------------------.
          | {', '.join(letter_list)}  |
          |____________________________|
          
          ''')

def show_results(valid_words, detailed=True):
    '''Takes a list of all valid words, displays the longest one/s along with letter count
    and shows a separate list of all other possible words in no particular order. '''
    longest = max([len(i) for i in valid_words])
    longest_words = [i for i in valid_words if len(i) == longest]
    print(f'The longest word is {longest} letters long.')
    print(', '.join(longest_words))
    if detailed:
        print('\nThis is the list of all possible words.\n')
        print(', '.join(valid_words))


def is_valid(contestant_word, valid_words):
    '''Takes the contestant word and checks if it is a valid word. if not, returns 0, if yes,
    returns the length of the word along with printing info about word to the console. '''
    if contestant_word not in valid_words:
        print(f'Sorry. {contestant_word} is not a valid word.')
        return 0 
    else:
        print(f'{contestant_word} is {len(contestant_word)} letters long and it is a valid choice.')
        return len(contestant_word)

def display_menu():
    '''Prints the instructions of the game along with the options menu. '''
    print('''
                                Welcome to Countdown!
                                ---------------------
                                
 - You choose a total of 9 letters. you can choose either vowels or consonants which will be randomly generated.
 - You have 30 seconds to make the longest word from the 9 letters supplied.
 - In single Player mode you play one round against the computer for practice. 
 - In two player mode, you play four rounds. 
 - The player with the longest valid word receives points equal to the word length. The opponent gets nothing.
 - In the event of a tie, both players recieve the points. If a player uses all 9 letters, 18 points are awarded. 
 - In conundrum, the players are given a scrambled 9-letter word and they must try to solve the word.

                                   Menu Options
                                -----------------
                                1. Single Player
                                2. Two Player
                                3. Conundrum
                                4. Quit
''')


#===================================Two player option==============================

def compare_score(p1, p2):
    '''Compares the players scores. If scores are equal, both are returned. if one is greater than
    the other, the former is returned unmodified and the latter is zeroed. '''
    if p1 == p2:
        return p1, p2
    elif p1 > p2:
        p2 = 0
        return p1, p2
    else:
        p1 = 0
        return p1, p2

#==================================Conundrum=======================================
def scrambler(word):
    '''Takes a str word, scrambles it, and returns a scrambled str. '''
    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled = ''.join(scrambled)
    return scrambled


#======================================main========================================

def main():
    game_running = True
    while game_running:
        display_menu()
        choice = check_menu_input(4)
        if choice == '1':
            letter_list = get_letters(vowels, consonants)
            format_letters(letter_list)            
            valid_words = possible_words(word_list, letter_list)
            counter()
            contestant_word = input('\nEnter your word: ')
            value = is_valid(contestant_word, valid_words)            
            show_results(valid_words)
            to_main = input('\nPress any key to return to the main menu.')
        if choice == '4':
            print('Thank you for playing countdown.')
            game_running = False
        if choice == '3':
            word = random.choice(conundrum_list)
            scrambled = scrambler(word)
            print('The Conundrum word is: ',scrambled)
            counter()
            guess = input('\nSolve the conundrum: ')
            if guess == word:
                print(f'congratulations! the word is {word}.')
            else:
                print(f'The word is {word}.')
            to_main = input('\nPress any key to return to the main menu.')
        if choice == '2':
            rounds = 1
            player_1 = input('Enter name for player 1: ')
            player_2 = input('Enter name for player 2: ')
            players = {player_1: 0, player_2: 0}
            while rounds < 5:
                if rounds % 2 != 0:
                    player = player_1
                else:
                    player = player_2
                print(f'Round {rounds}: {player} chooses the letters.')
                letter_list = get_letters(vowels, consonants)
                format_letters(letter_list)
                valid_words = possible_words(word_list, letter_list)
                counter()
                player_1_word = input(f'\n{player_1}, enter your word:\n')
                player_2_word = input(f'\n{player_2}, enter your word:\n')
                player_1_score = is_valid(player_1_word, valid_words)
                player_2_score = is_valid(player_2_word, valid_words)
                p1_score, p2_score = compare_score(player_1_score, player_2_score)
                show_results(valid_words, detailed=False)
                players[player_1] += p1_score
                players[player_2] += p2_score                
                print(f'Score for {player_1}: {players[player_1]}')
                print(f'Score for {player_2}: {players[player_2]}')
                rounds += 1
            to_main = input('\nPress any key to return to the main menu.')
            

if __name__ == '__main__':
    main()
