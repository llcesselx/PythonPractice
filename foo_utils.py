#!/usr/bin/env python3

version = "0.0.1"

foo_name = "Foo"


def foo_says(x):
    print(f"{foo_name}: {x}")


class Foo:
    def __init__(self):
        self.foo = "FOO"


if __name__ == "__main__":
    print(f'Running tests for "{__file__}" (v{version})...')

    foo_says("In future modules, these tests will be defined by you!")
    foo_name = "You"
    foo_says("Got it!")

    f1 = Foo()
    print(f1)
    print(hex(id(f1)))
    print(f1.foo)
