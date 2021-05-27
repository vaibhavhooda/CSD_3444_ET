"""
File used for string related manipulations.
"""


def reverse_name():
    name = input("Please enter your name: ")
    reversed_name = ""
    for i in range(len(name), 0, -1):
        reversed_name += name[i-1]
    print("Name in reverse order is: ", reversed_name)
