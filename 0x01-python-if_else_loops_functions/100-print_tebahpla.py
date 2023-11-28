#!/usr/bin/python3
for i in range(ord('z'), ord('A'), -1):
    if ord('a') <= i <= ord('z') or ord('A') <= i <= ord('Z'):
        print("{:c}".format(i), end="")
