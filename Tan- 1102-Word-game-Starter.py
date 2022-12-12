# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
#On this project I have collaborated with the following student(s) (if any) :Navy 

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)
    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
      if i in letters_guessed:
        pass
      else:
        return False
    return True



### Testcases
#print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
#print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
#print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    full_word = ""
    for letter in secret_word:
      if letter in letters_guessed:
        full_word += letter + " "
        pass
      else:
        full_word += "_ "
    return full_word
    

#Testcases
#print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
#print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))
#print(get_guessed_word ('grapefruit', ['k', 'm', 'b', 'j', 'e', 'w', 's', 'z', 'u', 'x']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters_not_guessed = string.ascii_lowercase
    for char in letters_guessed:
      letters_not_guessed = letters_not_guessed.replace(char, "")
    return letters_not_guessed
      
#Testcases 
#print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))
#print(get_available_letters(['r', 'y', 'd', 'u', 't']))

def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game.
    * At the start of the game, let the user know how many 
      letters the secret_word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Reading word_listfile...')
    print('55900 words found')
    print('Let the game begin!')
    letters_guessed = []
    number_of_guesses = 8
    end_game = False
    print("I am thinking of a word with", len(secret_word), "letters.")
    while number_of_guesses != 0 and end_game == False:
      print('You have', number_of_guesses, 'guesses left.')
      print('Letters avalible to you:', get_available_letters(letters_guessed).replace(" ", ""))
      guessing_letter = input("Guess a letter: ")
      if guessing_letter in letters_guessed:
        letters_guessed.append(guessing_letter)
        print('You fool! You tried this letter already: ', get_guessed_word(secret_word, letters_guessed))
      elif guessing_letter in list(secret_word):
        letters_guessed.append(guessing_letter)
        print('Correct:', get_guessed_word(secret_word, letters_guessed))
      else:
        letters_guessed.append(guessing_letter)
        print('Incorrect, this letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
        number_of_guesses -= 1
      print('')
      full_word = get_guessed_word(secret_word, letters_guessed)
      end_game = is_word_guessed(secret_word, letters_guessed)
      
    if number_of_guesses == 0:
      print("GAME OVER! ☹️")
      print('The secret word is:', secret_word)
    else:
      print("Congratulations!🥳 You have guessed the secret word🥳")



def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()
