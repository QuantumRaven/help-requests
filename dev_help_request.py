#!/usr/bin/env python3

import sys
import os


def clear_terminal():
    """Checks what operating system is in use: Windows or Linux.
    Then, it clears the terminal with the approriate command based
    on the operation system detected.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def bootdev_help_request():
    """This generates a help request for https://boot.dev/ lessons
    based on their provided formatting in Discord."""
    lesson_link = input("\nLesson link: ")

    print("\nNow, enter your text (press Ctrl+D to finish):\n")
    multiline_input = sys.stdin.read()
    clear_terminal()
    print(f"{lesson_link}\n\n{multiline_input}")


def theodinproject_help_request():
    """This generates a help request for https://theodinproject.com/ lessons
    based on their provided formatting in Discord and website."""
    lesson_link = input("\nLesson link: ")

    print("\nNow, enter your text (press Ctrl+D to finish):\n")
    multiline_input = sys.stdin.read()
    clear_terminal()
    print(f"{lesson_link}\n\n{multiline_input}")


def main():
    """Calls for the user to make a choice on what
    function they want to call based on available options."""
    while True:
        print("Choose a function to execute: ")
        print("1. Boot.Dev help request")
        print("2. TheOdinProject help request")
        print("3. Exit")

        choice = input("Enter your choice of 1, 2, or 3: ")

        if choice == "1":
            bootdev_help_request()
        elif choice == "2":
            theodinproject_help_request()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
