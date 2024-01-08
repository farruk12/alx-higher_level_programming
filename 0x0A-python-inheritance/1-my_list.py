#!/usr/bin/python3
"""Write a class MyList that inherits from list"""

class MyList(list):
    def print_sorted(self):
        """Print the list in sorted order (ascending)."""
        x = sorted(self)
        print(x)
