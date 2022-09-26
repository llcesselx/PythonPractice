#!/usr/bin/env python3

import sys

args = sys.argv[1:]

cols = 17
rows = 17
points = []
new_points = []

version = "1.0.1"

def help_menu():
    print("\n██████╗ ██╗      ██████╗ ████████╗██████╗ ██╗   ██╗")
    print("██╔══██╗██║     ██╔═══██╗╚══██╔══╝██╔══██╗╚██╗ ██╔╝")
    print("██████╔╝██║     ██║   ██║   ██║   ██████╔╝ ╚████╔╝ ")
    print("██╔═══╝ ██║     ██║   ██║   ██║   ██╔═══╝   ╚██╔╝  ")
    print("██║     ███████╗╚██████╔╝   ██║██╗██║        ██║   ")
    print("╚═╝     ╚══════╝ ╚═════╝    ╚═╝╚═╝╚═╝        ╚═╝  \n")
    print("               Commands:\n")
    print("-v  --version                  Version Number")
    print("-h  --help                     Help Menu\n")
    print("               Directions:\n")
    print("Enter arguments as an ordered pair to see them plotted")
    print("on the graph.")
    print("e.g. plot.py 2,3 -2,-1 -4,3 1,-5")
    exit(0)

if "-v" in args or "--version" in args:
    print(f"VERSION: {version}")
    exit(0)

if "-h" in args or "--help" in args:
    help_menu()

for arg in args:
    point = arg.split(",")
    x_value = int(point.pop(0))
    y_value = int(point.pop(0))
    points.append(x_value)
    points.append(y_value)
    print(points)

while len(points)>0:
    x = points.pop(0)
    print(x)
    y = points.pop(0)
    print(y)
    print(points)
    new_point = (x, y)
    print(new_point)
    new_points.append(new_point)
    print(new_points)

print(new_points)

for y in range(rows//2, -(rows//2)-1, -1):
    for x in range(-(cols//2), cols//2+1, 1):
        current_point=(x, y)
        if current_point in new_points:
            print("X",end="")
        elif (x == 0) and (y==0):
            print("+", end="")
        elif (y == 0) or (y == (cols//2)) or (y == -(cols//2)):
            print("-", end="")
        elif (x == 0) or (x == -(cols//2)) or (x == (cols//2)):
            print("|", end="")
        else:
            print(" ", end="")
    print()

# References: for-loop and pop-method not iterating over whole list:
# https://stackoverflow.com/questions/13939341/why-does-a-for-loop-with-pop-method-or-del-statement-not-iterate-over-all-list
