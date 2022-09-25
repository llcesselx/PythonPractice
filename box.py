#!/usr/bin/env python3

import sys

args = sys.argv[1:]
box = ""

version = "1.0.0"

def help_menu():
    print("\n██████╗  ██████╗ ██╗  ██╗   ██████╗ ██╗   ██╗")
    print("██╔══██╗██╔═══██╗╚██╗██╔╝   ██╔══██╗╚██╗ ██╔╝")
    print("██████╔╝██║   ██║ ╚███╔╝    ██████╔╝ ╚████╔╝ ")
    print("██╔══██╗██║   ██║ ██╔██╗    ██╔═══╝   ╚██╔╝")
    print("██████╔╝╚██████╔╝██╔╝ ██╗██╗██║        ██║")
    print("╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝        ╚═╝  \n")
    print("               Commands:\n")
    print("-v  --version                  Version Number")
    print("-h  --help                     Help Menu\n")
    print("               Directions:\n")
    print("This program will create a box. You may enter")
    print("your preferred dimensions in the arguments...")
    print("e.g. box.py 10 5")
    print("This will create a box with a WIDTH of the")
    print("first number and a HEIGHT of the second number.\n")
    print("Our example above would create a box like this:\n")
    print("+--------+     You can see the 10 characters at")
    print("|        |     the top and the bottom of the box")
    print("|        |     because we specified a column width")
    print("|        |     of 10. We will also see 5 characters")
    print("+--------+     going up and down because we specified")
    print("               a row height of 5.")

if "-v" in args or "--version" in args:
    print(f"VERSION: {version}")
    exit(0)

if "-h" in args or "--help" in args:
    help_menu()
    exit(0)

if len(args) == 0:
    args.insert(0,8)
    args.insert(1,8)

try:
    cols = int(args[0])
except ValueError:
    msg = "Need to enter integer, Columns (Width) set at 8"
    cols = 8
    print(msg, file=sys.stderr)
    pass

try:
    rows = int(args[1])
except ValueError:
    msg = "Need to enter integer, Rows (Height) set at 8"
    rows = 8
    print(msg, file=sys.stderr)
    pass

for y in range(rows):
    for x in range(cols):
        if (x == 0 and y == 0) or (x == 0 and y == rows-1):
            box+=("+")
        elif (x ==cols-1 and y == 0) or (x == cols-1 and y == rows-1):
            box+= ("+\n")
        elif (x > 0 and y == 0) or (x > 0 and y == rows-1):
            box += ("-")
        elif (x == 0 and y > 0):
            box += ("|")
        elif  (x == cols-1 and y > 0):
            box += ("|\n")
        else:
            box += (" ")

print(box)
print(f"COLUMNS: {cols}\nROWS: {rows}")
