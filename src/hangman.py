#!/usr/bin/env python3

import os
import random
import platform

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
def main():
    print("Lets play Hangman")
    words = ["Hochkuller", "Waschtheke", "Hochtüddlechen" ]
    guess_me = list(random.choice(words))
    guessed = ['_' for _ in range(len(guess_me))]
    lifepoints = 6
    lp = lifepoints

    while (('_' in guessed) and (lp > 0)):
        print(f"{' '.join(guessed).capitalize()}")
        if lp > 1:
            print(f"Du hast noch {lp} Lebenspunkte")
        if lp == 1:
            print(f"Du hast noch {lp} Lebenspunkt")

        guess = input(">>> ")[0].upper()
        correct = False

        for i in range(len(guess_me)):
            if guess == guess_me[i].upper():
                guessed[i] = guess
                correct = True
        if correct == False:
            lp -= 1

        clear

    print("You won!")

if __name__ == '__main__':
    main()
