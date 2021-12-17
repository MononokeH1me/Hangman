#!/usr/bin/env python3

import os
import random
import platform
import time
from typing import Tuple
import json

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def read_file(path: str) -> list:
    with open(path, mode='r') as file_handler:
        return [line.strip('\n') for line in file_handler.readlines()]

def print_slow(msg: str, end='') -> None:
    for char in msg:
        print(char, end=end, flush=True)
        time.sleep(0.05)

def color_string(msg: str, r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m{msg}\0330"

def load_game():
    print('\n'.join(read_file("src/splash.txt")))
    print_slow ("German, a very weird language")
    clear()

def main_menu():
    print_slow ("Choose a mode\n z = Zeuggame\n f = Funnygame\n s = Stuffgame\n")
    gamemode = input(">>> ")[0].upper()
    while gamemode != "Z" and gamemode != "F" and gamemode != "S":
        clear()
        print("Bitte gib einen gültigen Modus ein")
        gamemode = input(">>> ")[0].upper()


    if gamemode == "Z":
        dictionary = read_json('src/zeug.json')
    elif gamemode == "F":
        dictionary = read_file('src/words.txt')
    elif gamemode == "S":
        dictionary = read_json('src/prezeug.json')

    return (dictionary, gamemode)


def read_json(path: str) -> dict:
    with open(path, mode='r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def main(words: list) ->Tuple[int, str]:
    print("Let's play Hangman")
    guess_meword = random.choice(words)
    guess_me = list(guess_meword)
    guessed = ['_' for _ in range(len(guess_me))]
    max_lp = 10
    lp = max_lp

    while (('_' in guessed) and (lp > 0)):
        print(' '.join(guessed).capitalize())
        #print(f"{' '.join(guessed).capitalize()}")
        print('\n'.join(read_file(f"src/{max_lp - lp}.txt")))
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
        if not correct:
            lp -= 1

        clear()

    return (lp, guess_meword)


def credits(lp: int, guess_meword: str, mode: str) -> None:
    lost = ("You lost!")
    won = ("You won!")
    red = (138, 3, 3)
    green = (24, 143, 0)
    if lp > 0:
        print(color_string(won, *green))
    if lp == 0:
        print(color_string(lost, *red))
    #print(color_string(lost, *red if lp == 0 else *green))
    print("\033[39mThe word was:\n {}".format(guess_meword))
    if mode == "Z" or mode == "S":
        for index, translation in enumerate(dictionary[guess_meword]):
            print(f" {index+1:2}) {translation}")

if __name__ == '__main__':
    load_game()
    dictionary, gamemode = main_menu()
    words = list(dictionary)
    game_data = main(words)
    credits(lp=game_data[0], guess_meword=game_data[1], mode=gamemode[0])

