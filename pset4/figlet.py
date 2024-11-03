from pyfiglet import Figlet
from random import choice
import sys

if len(sys.argv) == 1:
    font = choice(font_list)
elif len(sys.argv) == 2:
    sys.exit("Not enough arguments")
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in font_list:
            font = sys.argv[2]
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")

figlet = Figlet()
font_list = figlet.getFonts()
figlet.setFont(font=font)

print(figlet.renderText(input("Input: ")))


