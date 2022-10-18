#!/usr/bin/env python3

import sys

args = sys.argv[1:-1]
version = "1.10.7"


def help_menu():
    print("-h  --help              open help text")
    print("-v  --version           version number")

def in_parens(test):
    search_terms = "".join(test)
    try:
        start_parens = search_terms.index("(")
        new_search_terms = search_terms[start_parens+1:]
    except ValueError:
        print(file=sys.stderr)
        return None
        exit(1)
    try:
        end_parens = new_search_terms.index(")")
        fin_search_terms = new_search_terms[:end_parens]
    except ValueError:
        print(file=sys.stderr)
        return None
        exit(1)
    return fin_search_terms

if "-v" in args or "--version" in args:
    print(version)
    exit(0)
if "-h" in args or "--help" in args:
    help_menu()
    exit(0)
if "-f" in args or "--file" in args:
    pass

if __name__ == "__main__":
    search_terms = "".join(args)
    in_parens()

    class ClassName(object):
        """docstring for ClassName"""
        def __init__(self, arg):
            super(ClassName, self).__init__()
            self.arg = arg
