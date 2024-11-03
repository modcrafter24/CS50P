from pyfiglet import Figlet
from random import choice
import sys

if len(sys.argv) > 3:
    sys.exit("Too many arguments")
elif len(sys.argv) == 2:
    sys.exit("Not enough arguments")

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    font = choice(font_list)
if len(sys.argv) == 3:
    if argv[1] == '-f' or argv[1] == '--font':
        if argv[2] in font_list:
            font = argv[2]
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

figlet.setFont(font=font)

input_string = input("Input: ")

print(figlet.renderText(input_string))


