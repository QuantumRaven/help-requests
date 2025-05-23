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


def boot_dev_help_request():
    """This generates a help request for https://boot.dev/ lessons
    based on their provided formatting in Discord."""
    lesson_link = input("\nLesson link: ")

    print("\nNow, enter your text (press Ctrl+D to finish):\n")
    multi_line_input = sys.stdin.read()
    clear_terminal()
    print(f"{lesson_link}\n\n{multi_line_input}")
    return multi_line_input


def the_odin_project_help_request():
    """This generates a help request for https://theodinproject.com/ lessons
    based on their provided formatting in Discord and website."""
    lesson_link = input("\nLesson link: ")

    print("\nNow, enter your text (press Ctrl+D to finish):\n")
    multi_line_input = sys.stdin.read()
    clear_terminal()
    print(f"{lesson_link}\n\n{multi_line_input}")
    return multi_line_input


def main():
    """Calls for the user to make a choice on what
    function they want to call based on available options."""
    while True:
        print("Choose a function to execute: ")
        print("boot_dev")
        print("the_odin_project")
        print("exit")

        choice = input("\nEnter your choice of boot_dev, the_odin_project, or exit: ")

        if choice == "boot_dev":
            clear_terminal()
            multi_line_input = boot_dev_help_request()
            with open("boot_dev.md", "w") as file:
                file.write(multi_line_input)
            break
        elif choice == "the_odin_project":
            clear_terminal()
            multi_line_input = the_odin_project_help_request()
            with open("the_odin_project.md", "w") as file:
                file.write(multi_line_input)
            break
        elif choice == "exit":
            clear_terminal()
            print("exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
