#!/usr/bin/env python3

import sys

#VERSION CONTROL
version_number = "1.0.0"

#Variables------------------------------------------------
args = sys.argv[1:]
sum_result = 0

#Program functions--------------------------------------
def title():
    print("")
    print("  aaaaaaaaaaaaavvvvvvv           vvvvvvvggggggggg   ggggg        ppppp   pppppppppyyyyyyy           yyyyyyy")
    print("  a::::::::::::av:::::v         v:::::vg:::::::::ggg::::g        p::::ppp:::::::::py:::::y         y:::::y ")
    print("  aaaaaaaaa:::::av:::::v       v:::::vg:::::::::::::::::g        p:::::::::::::::::py:::::y       y:::::y  ")
    print("           a::::a v:::::v     v:::::vg::::::ggggg::::::gg        pp::::::ppppp::::::py:::::y     y:::::y   ")
    print("    aaaaaaa:::::a  v:::::v   v:::::v g:::::g     g:::::g          p:::::p     p:::::p y:::::y   y:::::y    ")
    print("  aa::::::::::::a   v:::::v v:::::v  g:::::g     g:::::g          p:::::p     p:::::p  y:::::y y:::::y     ")
    print(" a::::aaaa::::::a    v:::::v:::::v   g:::::g     g:::::g          p:::::p     p:::::p   y:::::y:::::y      ")
    print("a::::a    a:::::a     v:::::::::v    g::::::g    g:::::g          p:::::p    p::::::p    y:::::::::y       ")
    print("a::::a    a:::::a      v:::::::v     g:::::::ggggg:::::g          p:::::ppppp:::::::p     y:::::::y        ")
    print("a:::::aaaa::::::a       v:::::v       g::::::::::::::::g  ......  p::::::::::::::::p       y:::::y         ")
    print(" a::::::::::aa:::a       v:::v         gg::::::::::::::g  .::::.  p::::::::::::::pp       y:::::y          ")
    print("  aaaaaaaaaa  aaaa        vvv            gggggggg::::::g  ......  p::::::pppppppp        y:::::y           ")
    print("                                                 g:::::g          p:::::p               y:::::y            ")
    print("                                     gggggg      g:::::g          p:::::p              y:::::y             ")
    print("                                     g:::::gg   gg:::::g         p:::::::p            y:::::y              ")
    print("                                      g::::::ggg:::::::g         p:::::::p           y:::::y               ")
    print("                                       gg:::::::::::::g          p:::::::p          yyyyyyy                ")
    print("                                         ggg::::::ggg            ppppppppp                                 ")
    print("                                            gggggg                                                         \n")

def help_menu():
    print("")
    title()
    print("")
    print("This program will take input from three different sources. It can take it as either argument data from the")
    print("command line, it can take it as input from a keyboard if the user is at the terminal or it can take data from")
    print("a file or other data source and it can pipe that data into the program as input.\n")
    print("If user is at terminal enter: avg.py (Instructions will be given)")
    print("If user is piping in data from file or terminal, enter: <PREV COMMANDS> | avg.py")
    print("If data is given in argument data, then enter: avg.py <ARG> <ARG> <ARG> etc.\n")
    print("                                                Commands:\n")
    print("-v  --version                                                                               version number")
    print("-h  --help                                                                                  help menu")
    print("")
    print("VERSION: " + version_number)
    exit(0)

def is_a_tty():
    user_data = "0"
    numbers = 0
    number_list= []
    numbers_mean = 0

    while user_data != "":
        try:
            user_data = input("Enter a number: ")
            numbers += float(user_data)
            number_list.append(user_data)
            print(numbers)
            print(number_list)
        except ValueError:
            break

    if user_data == "":
        numbers_mean = numbers / (len(number_list))
        pass

    print("Avg = ", numbers_mean)
    exit(0)

def is_a_pipe():
    for line in sys.argv:
        print(line)
        exit(0)

#Options and arguments------------------------------------
if "-v" in args or "--version" in args:
    print("VERSION: " + version_number)
    exit(0)

if "-h" in args or "--help" in args:
    help_menu()
    exit(0)

#Argument data---------------------------------------------
if len(args) > 0:
    for arg in args:
        sum_result +=float(arg)

    avg_result = sum_result/len(args)
    print("Average of all given numbers: ", avg_result)
    exit(0)
elif sys.stdin.isatty:
    is_a_tty()
else:
    is_a_pipe()

#TTY or PIPE data------------------------------------------
