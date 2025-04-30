#!/usr/bin/env python3

import sys
import os
from simple_term_menu import TerminalMenu


def clear_terminal():
    """Checks what operating system is in use: Windows or Linux.
    Then, it clears the terminal with the approriate command based
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
    print("""
    Answer the following questions:

    What do you think the problem is?
    What exactly do you want to happen?
    What is actually happening?
    How did you get there?
    What have you tried so far?
    """)
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
        options = ["boot_dev", "the_odin_project", "exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        chosen_one = options[menu_entry_index]

        if chosen_one == "boot_dev":
            clear_terminal()
            selection_option(chosen_one)
            multi_line_input = boot_dev_help_request()
            with open("boot_dev.md", "w") as file:
                file.write(multi_line_input)
        elif chosen_one == "the_odin_project":
            clear_terminal()
            selection_option(chosen_one)
            multi_line_input = the_odin_project_help_request()
            with open("the_odin_project.md", "w") as file:
                file.write(multi_line_input)
        elif chosen_one == "exit":
            clear_terminal()
            selection_option(chosen_one)
            print(f"You've selected {chosen_one}.")
            print("exiting program...")
            sys.exit()
        else:
            print("Invalid chosen_one. Please try again.")


if __name__ == "__main__":
    main()
