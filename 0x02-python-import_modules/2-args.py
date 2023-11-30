#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    print("{} argument{}.".format(num_args, '' if num_args == 1 else 's'))
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
