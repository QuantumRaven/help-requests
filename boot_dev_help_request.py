#!/usr/bin/env python3

import sys, os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")

def help_request():
    lesson_link = input("\nLesson link: ")    

    print("\nNow, enter your text (type 'END' on a new line to finish):\n")
    multiline_input = sys.stdin.read()
    clear_terminal()
    print(f"{lesson_link}\n\n{multiline_input}")

help_request()
