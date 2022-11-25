#!/usr/bin/env python3

import sys

#VERSION CONTROL
version_number = "0.0.2"

#HELP MENU
def help_menu():
    print("  _____                                      ")
    print(" |  __ \                                     ")
    print(" | |__) |__ _ __ _ __ ___  ___   _ __  _   _ ")
    print(" |  ___/ _ \ '__| '_ ` _ \/ __| | '_ \| | | |")
    print(" | |  |  __/ |  | | | | | \__ \_| |_) | |_| |")
    print(" |_|   \___|_|  |_| |_| |_|___(_) .__/ \__, |")
    print("                                | |     __/ |")
    print("                                |_|    |___/ \n\n")
    print("Instructions: Enter arguments after calling program in terminal.\n")
    print("For example: root@PC:~# perms.py -r -write \n")
    print("               Commands:\n               ")
    print("-h  --help                   help menu")
    print("-v  --version                version number")
    print("")
    print("          Permission Commands:\n   ")
    print("-r  --read                   give read permission")
    print("-w  --write                  give write permission")
    print("-x  --execute                give execute permission")

#System argument options
if "-v" in sys.argv or "--version" in sys.argv:
    print(version_number)
    exit(0)

if "-h" in sys.argv or "--help" in sys.argv:
    help_menu()
    exit(0)

#Permission variables
r = "-r" in args or "--read" in args
w = "-w" in args or "--write" in args
x = "-x" in args or "--execute" in args

total = 0

exe = 1
wri = 2
rea = 4

if r:
    total += rea
if w:
    total += wri
if x:
    total += exe

print(r, w, x)

print(total)

