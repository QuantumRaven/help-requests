#!/usr/bin/env python3

import sys

def help_request():
    lesson_link = input("\nLesson link: ")    

    print("\nNow, enter your text (type 'END' on a new line to finish):\n")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    text = "\n".join(lines)
    return lesson_link, text

lesson_link, text = help_request()
output = f"Lesson link: {lesson_link}\n\n{text}"
print(output)
