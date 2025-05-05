#!/usr/bin/env python3

import sys
import os


def clear_terminal():
    """Checks what operating system is in use: Windows or Linux.
    Then, it clears the terminal with the appropriate command based
    on the operating system detected.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def selection_option(chosen_one):
    print(f"You've selected {chosen_one}.")


"""
Boot.Dev
"""


def boot_dev_help_request():
    """This generates a help request for https://boot.dev/ lessons
    based on their provided formatting in Discord."""
    lesson_link = input("\nLesson link: ")

    print("\nNow, enter your text (press Ctrl+D to finish):\n")
    multi_line_input = sys.stdin.read()
    clear_terminal()
    print(f"{lesson_link}\n\n{multi_line_input}")
    return multi_line_input


"""
The Odin Project
"""


def the_odin_project_help_request():
    """This generates a help request for https://theodinproject.com/ lessons
    based on their provided formatting in Discord and website."""
    print(
        """
    Answer the following questions:

    What do you think the problem is?
    What exactly do you want to happen?
    What is actually happening?
    How did you get there?
    What have you tried so far?
    """
    )
    lesson_link = input("\nLesson link: ")

    print("\nNow, enter your text (press Ctrl+D to finish):\n")
    multi_line_input = sys.stdin.read()
    clear_terminal()
    print(f"{lesson_link}\n\n{multi_line_input}")
    return multi_line_input


def main():
    """Calls for the user to make a chosen_one on what
    function they want to call based on available options."""

    while True:
        option = input("\nEnter your choice of boot_dev, the_odin_project, or exit: ")

        if option == "boot_dev":
            clear_terminal()
            selection_option(option)
            multi_line_input = boot_dev_help_request()
            with open("boot_dev.md", "w") as file:
                file.write(multi_line_input)
        elif option == "the_odin_project":
            clear_terminal()
            selection_option(option)
            multi_line_input = the_odin_project_help_request()
            with open("the_odin_project.md", "w") as file:
                file.write(multi_line_input)
        elif option == "exit":
            clear_terminal()
            selection_option(option)
            print(f"You've selected {option}.")
            print("exiting program...")
            sys.exit()
        else:
            print("Invalid chosen_one. Please try again.")


if __name__ == "__main__":
    main()
