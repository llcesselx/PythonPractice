#!/usr/bin/env python3

import sys
import json

#Version Control
version_number = "VERSION: 0.1.1"

#Title
def title():
    print(" __                                         .___                                                 ")
    print("|  | __ ____ ___.__.__  _  _____________  __| _/    _____ _______  ____  ______    ______ ___.__.")
    print("|  |/ // __ <   |  |\ \/ \/ /  _ \_  __ \/ __ |     \___  \\_  __ \/ ___\/  ___/    \____ <   |  |")
    print("|    <\  ___/\___  | \     (  <_> )  | \/ /_/ |      / __ \|  | \/ /_/  >___ \     |  |_> >___  |")
    print("|__|_ \\___  >  ____|  \/\_/ \____/|__|  \____ |_____(____  /__|  \___  /____  > /\ |   __// ____|")
    print("     \/    \/\/                              \/_____/    \/     /_____/     \/  \/ |__|   \/     ")
    print("")

#Help menu
def help_menu():
    title()
    print("HELP MENU:\n")
    print("-h  --help                  help")
    print("-v  --version               version\n")
    print("Instructions:\n  Enter arguments in format, -label value --label value etc. The user MUST enter arguments.\n")
    print("NOTE: Arguments MUST be entered exactly as formatted in example below.\n")
    print("Example:")
    print("  keyword_args.py --fruit=banana -veggie=tomato -my_age=29 -inches=63.75")

#JSON print
def jprint(item):
    print(json.dumps(item, indent=4))

#-----------------------------------------------------------------------------------------------------------------------------
# Beginning
#-----------------------------------------------------------------------------------------------------------------------------
args = sys.argv[1:]

#Run options first, check to make sure user entered arguments
if "-v" in args or "--version" in args:
    print(version_number)
    exit(0)

if "-h" in args or "--help" in args:
    help_menu()
    exit(0)

if len(args) == 0:
    msg = "ERROR: MUST ENTER ARGUMENTS!!! Arguments may not remain empty."
    print(msg, file=sys.stderr)
    exit(1)

#If program runs successfully, the title will show first
title()

argument_dict = {}

for arg in args:
    new_args = arg.split("=")

    label = new_args.pop(0)
    value = new_args.pop(0)

    label = label.strip("-")

    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            pass

    argument_dict[label] = value

jprint(argument_dict)
