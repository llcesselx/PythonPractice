#!/usr/bin/env python3

import sys
import json

#VERSION CONTROl
version_number = "0.0.2"

#HELP MENU
def help_menu():
    print("_    ____ ___  ____ _    ____ ___      ___  ____ _ ____ ____  ___  _   _ ")
    print("|    |__| |__] |___ |    |___ |  \     |__] |__| | |__/ [__   |__]  \_/  ")
    print("|___ |  | |__] |___ |___ |___ |__/ ___ |    |  | | |  \ ___] .|      |   ")
    print("")
    print("A program to place labeled pairs of arguments into a dictionary.")
    print("Arguments are expected in the form -label, value --label, value, etc.")
    print("Example:")
    print("   ./labeled_pairs.py --fruit grapes --veggie cucumber -c 47°")
    print("")
    print("                          Commands:\n")
    print("-v  --version                                     version number")
    print("-h  --help                                        help menu")
    print("")
    print("VERSION: " + version_number)
    exit(0)

#JSON Print function
def jprint(item):
    print(json.dumps(item, indent=4))


#****************************************************************************
#Beginning
#****************************************************************************
args = sys.argv[1:]

if "-v" in args or "--version" in args:
    print("VERSION: " + version_number)
    exit(0)

if "-h" in args or "--help" in args:
    help_menu()
    exit(0)

if len(args) == 0:
    msg = "Must contain arguments of the form -label, value, -label, value, etc."
    print(msg, file=sys.stderr)
    exit(1)

di = {}

while len(args):
    label = args.pop(0)
    value = args.pop(0)

    label = label.strip("-")

    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            pass

    di[label] = value

jprint(di)
