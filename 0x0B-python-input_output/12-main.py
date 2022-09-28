#!/usr/bin/python3
"""
This project is for pascal trainagle
that returns a list of lists of integers representing 
the Pascal’s triangle of n
"""

pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
     """print triangle function"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
