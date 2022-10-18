#!/usr/bin/env python3

import sys
import parens

version = "12.12.12"

def tty_mode():

    test = input()

    search_terms = "".join(test)

    try:
        start_parens = search_terms.index("(")
        new_search_terms = search_terms[start_parens+1:]
    except ValueError:
        msg = " no ( found"
        print(msg, file=sys.stderr)
        return None
        exit(1)
    try:
        end_parens = new_search_terms.index(")")
        fin_search_terms = new_search_terms[:end_parens]
    except ValueError:
        msg = "no ) found"
        print(msg, file=sys.stderr)
        return None
        exit(1)
    print(fin_search_terms)
    return fin_search_terms

def pipe_mode():
    pass

if __name__ == "__main__":
    args = sys.argv[1:]

    if "-h" in args or "--help" in args:
        print("-h  --help         help menu")
        print("-v  --version      version")

    if "-v" in args or "--version" in args:
        print(version)

    if sys.stdin.isatty():
        tty_mode()
    else:
        pipe_mode()
