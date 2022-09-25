#!/usr/bin/env python3

import sys
import random

version_number = "1.0.1"

def title():
    print("")
    print("██████   █████  ███    ██ ██████     ██████  ██    ██ ")
    print("██   ██ ██   ██ ████   ██ ██   ██    ██   ██  ██  ██  ")
    print("██████  ███████ ██ ██  ██ ██   ██    ██████    ████   ")
    print("██   ██ ██   ██ ██  ██ ██ ██   ██    ██         ██    ")
    print("██   ██ ██   ██ ██   ████ ██████  ██ ██         ██    ")
    print("")

def help_menu():
    title()
    print("")
    print("Instructions: Enter arguments to randomly generate numbers between")
    print("set min and max values. To set min and max values, enter arguments")
    print("as -m or --min for minimum values and -M or --max for maximum values.\n")
    print("If no min or max is set, default values for min is 0 and default")
    print("values for max is 100.\n")
    print("Example:")
    print("rand.py --min 5.5 -M 35.9\n")
    print("                          Commands:\n")
    print("-v  --version                                     version number")
    print("-h  --help                                        help menu\n")
    print("-m [ENTER MIN NUM]  --min [ENTER MIN NUM]         set minimum number")
    print("-M [ENTER MAX NUM]  --max [ENTER MAX NUM]         set maximum number")
    print("")
    print("VERSION: " + version_number)
    exit(0)

args = sys.argv[1:]
quant = sys.argv[-1]

min_number = 0.0
max_number = 100.0

try:
    iterations = int(quant)
except IndexError:
    iterations = 1
except ValueError:
    iterations = 1

if "-v" in args or "--version" in args:
    print("VERSION: " + version_number)
    exit(0)

if "-h" in args or "--help" in args:
    help_menu()
    exit(0)

if "-m" in args or "--min" in args:
    try:
        min_index = args.index("-m")+1
    except ValueError:
        try:
            min_index = args.index("--min")+1
        except ValueError:
            pass
    min_number = float(args[min_index])
else:
    min_number = 0.0

if "-M" in args or "--max" in args:
    try:
        max_index = args.index("-M")+1
    except ValueError:
        try:
            max_index = args.index("--max")+1
        except ValueError:
            pass
    max_number = float(args[max_index])
else:
    max_number = 100.0

#print(min_number, max_number)

#print(iterations)

for i in range(iterations):
    r = random.uniform(min_number, max_number)
    print(r)


