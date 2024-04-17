import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) > 3:
    sys.exit("Invalid usage")

if len(sys.argv) > 1:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")

str = input("Input: ")

if len(sys.argv) == 1:
    random_font = random.choice(figlet.getFonts())
    f = figlet.setFont(font=random_font)
    print(figlet.renderText(str))

elif sys.argv[2] in figlet.getFonts():
    f = figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(str))
