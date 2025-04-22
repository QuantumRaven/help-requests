#!/usr/bin/env python3

import sys, os

def clear_terminal():
    """Checks what operation system is in use: Windows or Linux.
    Then, it clears the terminal with the approriate command based
    on the operation system detected.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")

def bootdev_help_request():
    """This generates a help request for https://boot.dev/ lessons
    based on their provided formatting in Discord."""
    lesson_link = input("\nLesson link: ")    

    print("\nNow, enter your text (type 'END' on a new line to finish):\n")
    multiline_input = sys.stdin.read()
    clear_terminal()
    print(f"{lesson_link}\n\n{multiline_input}")


