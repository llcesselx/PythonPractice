#!/usr/bin/env python3

import sys

#Version Control
version_number = "0.0.1"

#If user enters -h or --help, the program will list the options and arguments the program can process
if "--help" in sys.argv or "-h" in sys.argv:
    #Pretty-fication of the console program
    print("***************************************")
    print("*                                     *")
    print("*      Program to list arguments      *")
    print("*                                     *")
    print("***************************************")
    print("             Commands:")
    print("")
    print("-h or --help                help ")
    print("-v or --version             version number")
    print("")
    print("            Instructions:")
    print("")
    print("Enter a list of objects as arguments. For an item\nwith a space, surround the item with quotes. The\n program will then list the items in a column.")
    print("")
    print("If you would like to save this list to a text\nfile, you should use the > FILE_NAME.txt after\nyour listed arguments.")
    print("")
    print("For Example:")
    print("You can type ./get_args.py pineapple apples > grocery.txt\nand it will be saved as an easy to\nread list!")
    exit(0)

#If user enters -v or --version, the program will print the version number
if "--version" in sys.argv or "-v" in sys.argv:
    print(version_number)
    exit(0)

try:
    sys.argv[0]
except ValueError:
    print("You must provide arguments to this program.", file=sys.stderr)
    exit(1)

#Establishing the variable args as the arguments passed minus the program itself
args = (sys.argv[1:])

#Print the items of the list arg, in a list on a new line.
print (*args, sep = "\n")
exit(0)


#References:
#   1. Printing lists in Python
#      -- https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/f

