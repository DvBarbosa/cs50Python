import sys
import random
from pyfiglet import Figlet


def print_usage_and_exit():
    print("Error: invalid arguments. Usage: ")
    print("python3 <script.py>")
    print("OR")
    print("python3 <script.py> -f/--font <font_name>")
    sys.exit(1)


def get_font(font_name=None):
    figlet = Figlet()
    if font_name is not None:
        fonts = figlet.getFonts()
        if font_name in fonts:
            figlet.setFont(font=font_name)
        else:
            print(f"Error: Font '{font_name}' not found.")
            print(f"Available fonts: {', '.join(fonts)}")
            sys.exit(1)
    else:
        fonts = figlet.getFonts()
        font_name = random.choice(fonts)
        figlet.setFont(font=font_name)
    return font_name


def main():
    font_name = None
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == "-h" or arg == "--help":
            print_usage_and_exit()
        else:
            print_usage_and_exit()
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font_name = sys.argv[2]
        else:
            print_usage_and_exit()

    font_name = get_font(font_name)

    text = input("Enter text to be printed in ASCII art: ")
    figlet = Figlet(font=font_name)
    ascii_art = figlet.renderText(text)
    print(ascii_art)


if __name__ == "__main__":
    main()
