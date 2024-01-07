from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

argv_len = len(sys.argv)
if argv_len == 1:
    font = choice(fonts)
else:
    if argv_len != 3:
        sys.exit("Invalid usage")

    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")

    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")

    font = sys.argv[2]


figlet.setFont(font=font)
text = input("Input: ")
print("Output: ", figlet.renderText(text), sep="\n")
