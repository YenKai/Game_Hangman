# Hangman game
#
# -----------------------------------
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    check = 0
    for word in secretWord:
        if word in lettersGuessed:
            check += 1
    
    if check == len(secretWord):
        return True
    else:
        return False       


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result=""
    for word in secretWord:
        if word in lettersGuessed:
            result = result + word 
        else:
            result = result + "_ "
    

    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    all_letters = string.ascii_lowercase[:]
    for word in lettersGuessed:
        
        all_letters = all_letters.replace(word,"")
    
    return all_letters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ',len(secretWord),' letters long.')
    lettersGuessed = ""
    life = 8;
    while not isWordGuessed(secretWord, lettersGuessed):
        print('-------------')
        print('You have ',life,' guesses left')
        print('Available letters: ',getAvailableLetters(lettersGuessed))	
        a = input("Please guess a letter: ").lower()
        if a in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        else:        
            lettersGuessed = lettersGuessed + a
            if a in secretWord:               
                print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
                life -= 1
                if life == 0:
                    break
                        
    print('------------')
    if life > 0:
        print("Congratulations, you won!")
    else: 
        print("Sorry, you ran out of guesses. The word was else.")    



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
