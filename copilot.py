# Make a hangman game

def hangman():
    import random
    import os
    import time
    import sys

    # Set up the game
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    wrong_guesses = 0
    stages = ["",
              "_________          ",
              "|               ",
              "|        |       ",
              "|        0       ",
              "|       /|\      ",
              "|       / \      ",
              "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    time.sleep(1)
    print("I'm thinking of a word that is", len(word), "letters long.")
    time.sleep(1)
    print("You have", 8, "guesses to get the word.")
    time.sleep(1)
    print("Ready? Let's go!")
    time.sleep(1)

    # Play the game
    while wrong_guesses < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong_guesses += 1
        print((" ".join(board)))
        e = wrong_guesses + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

hangman()