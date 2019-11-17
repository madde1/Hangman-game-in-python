# Hangman game in python with random words generated. 
import time
from random_word import RandomWords

name = input("What is your name? ")

print("Hello, " + name, "Time to play hangman!")

print ("")

time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# Makes random word everytime the game is played
randomWords = RandomWords()
words=""
words += randomWords.get_random_word()

prevGuess = list()
guesses = ""

turns = 10

while turns > 0:
    failed = 0
    for char in words: 
        if char in guesses: 
            print(char, end='')
        else:
            print("_ ", end = '')
            failed += 1
    if failed == 0:
      print("woohoo you just won!")
      print(words)
      break

    print(" ")
    guess = input("Guess a charachter: ")

    guesses += guess

    print("Previously guessed charachters: ")
    prevGuess.append(guess)
    print(prevGuess)

    if guess not in words: 
        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses")
    if turns == 0: 
        print("You just lost :( !")
        print(words)
