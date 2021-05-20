"""
This is a utility python script, which will provide following three features:
1. Compute area of a circle
2. Display name in reverse order
3. Print current date/time

Submitted By: Vaibhav Hooda (C0806432)
"""

from datetime import datetime

# Constant
PI = 3.14


def compute_area():
    radius = input("Please enter the radius of circle: ")
    try:
        radius = float(radius)
    except ValueError:
        print("Non numeric value entered, Terminating.....")
        exit()

    area = PI * radius * radius
    print(f"Area of the circle with radius{radius} is: {area}")


def reverse_name():
    name = input("Please enter your name: ")
    reversed_name = ""
    for i in range(len(name), 0, -1):
        reversed_name += name[i-1]
    print("Name in reverse order is: ", reversed_name)


def display_date_time():
    print(f"Current date/time is: {datetime.now()}")


def menu():

    print("Welcome to the utility program: \n"
          "1. Compute area of a circle.\n"
          "2. Display name in reverse order.\n"
          "3. Display current Date/Time.\n"
          "Press * to exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        compute_area()
    elif choice == "2":
        reverse_name()
    elif choice == "3":
        display_date_time()
    elif choice == "*":
        exit()
    else:
        print("Invalid choice, please try again......")
    menu()


if __name__ == '__main__':
    menu()
