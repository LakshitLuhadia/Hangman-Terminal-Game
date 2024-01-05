
import random

# You can add custom words to the text file to customize the game
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    
    inFile = open(WORDLIST_FILENAME, 'r')
    
    line = inFile.readline()
    
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: the word the user is guessing
    lettersGuessed: letters that have been guessed so far
    '''
    
    for letters in secretWord:
      if letters not in lettersGuessed:
        return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    
    word = ""
    for letter in secretWord:
      if letter in lettersGuessed:
        word += letter + " "
      else:
        word += "_ "
    return word


import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: letters that have been guessed so far
    returns: letters that have not yet been guessed.
    '''
    AvLetters = ""
    for alphabets in string.ascii_lowercase:
      if alphabets not in lettersGuessed:
        AvLetters += alphabets
    return AvLetters
    

def hangman(secretWord):

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")
    
    guessesAvailable = 8 #Customize the game by changing the maximum number of guesses available
    lettersGuessed = []
    
    while guessesAvailable > 0:
      print("You have " + str(guessesAvailable) + " guesses left.")
      print("Available letters: " + getAvailableLetters(lettersGuessed))
      guess = input("Please guess a letter: ").lower()
      if guess not in lettersGuessed:
        lettersGuessed.append(guess)
        if guess in secretWord:
          print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
          
        else:
          print("That letter is not in the word: " + getGuessedWord(secretWord, lettersGuessed))
          guessesAvailable -= 1
          
      else:
        print("You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        
      print("------------")
      if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
        return None
    
    print("Sorry, you ran out if guesses. The word was " + secretWord + ".")
    return None


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
